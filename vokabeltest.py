import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser(description="Erstelle einen Vokabeltest. Nutze '| pbcopy', um direkt in die Zwischenablage zu kopieren.")
    parser.add_argument('size', type=int, help='Anzahl abgefragter Vokabeln', metavar='n', default=16)
    parser.add_argument('--la', help="Falls der Test aus der gekürzten Liste erstellt werden soll. Dann Vokabelrange nur (1,26).", action="store_true")
    parser.add_argument('lektionen', type=int, nargs='*', default=range(1,27), help='Lektionen, aus denen die abgefragten Woerter kommen', choices=range(1,27))
    parser.add_argument("--solution", action="store_true", help="displays solution on new page")
    args = parser.parse_args()

    #wählt richtige Liste
    if args.la:
        df = pd.read_csv("Kreuzer_LABA_2025.csv")
    else:
        df = pd.read_csv("Vokabelliste_MagTheol_2025.csv")

    set = df[df.lektion.isin(args.lektionen)]
    n = args.size
    df_sub = set.sample(n)
    #print("\\section{Vokabeltest mit " + str(args.size) + " Vokabeln aus Lektion " + str(args.lektionen) + "}")
    print("\\section{Vokabeltest}")
    print("\\begin{multicols}{2}")
    print("{\\setstretch{1.7} \\raggedright")
    for i in range(n):
        if(pd.isna(df_sub.iloc[i]['bemerkungen'])):
            print("\\LargeHebrew{" + df_sub.iloc[i]['hebraeisch'] + "}\\\\")
        else:
            print(df_sub.iloc[i]['bemerkungen'] + " \\LargeHebrew{" + df_sub.iloc[i]['hebraeisch'] + "}\\\\")
    print("}")
    print("\\end{multicols}")

    if args.solution:
        print("\\newpage")
        print("\\subsection{Vokabeltest Lösungen}")
        print("\\begin{multicols}{2}")
        print("{\\setstretch{1.7} \\raggedright")
        for i in range(n):
            if (pd.isna(df_sub.iloc[i]['bemerkungen'])):
                print("\\LargeHebrew{" + df_sub.iloc[i]['hebraeisch'] + "}      " + df_sub.iloc[i]['deutsch'] + "\\\\")
            else:
                print(df_sub.iloc[i]['bemerkungen'] + " \\LargeHebrew{" + df_sub.iloc[i]['hebraeisch'] + "}     " + df_sub.iloc[i]['deutsch'] + "\\\\")
        print("}")
        print("\\end{multicols}")

if __name__ == "__main__":
    main()
