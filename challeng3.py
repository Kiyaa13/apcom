BankSoal = [
    {
        "soal" : "presiden pertama RI adalah",
        "opsional" : ["A.habibie", "B.soekarno", "C.soeharto", "D.jokowidodo"],
        "key" : "B"
    },
      {
        "soal" : "ibukota sumatera selatan",
        "opsional" : ["A.jakarta", "B.lampung", "C.palembang", "D.bandung"],
        "key" : "c"
    },
      {
        "soal" : "fotosintesis secara gelap terjadi di",
        "opsional" : ["A.stroma", "B.usus", "C.ribosom", "D.mitokondria"],
        "key" : "A"
    },
    
]

def Quiz( Prm_BankSoal ):
    score = 0
    for soalLoop in Prm_BankSoal:
        print( soalLoop["soal"])
        for opsiLoop in soalLoop["OpsiSoal"]:
            print( opsiLoop )
        answer = input("jawaban (a/b/c/d) :").upper()
        if answer == soalLoop["key"]:
            score = score + 1
            print("true")
        else:
            print(f"false !, jawaban yang tepat adalah{soalLoop['key']} ")
    print(f"jawaban benar {score} dari jumla soal {len(BankSoal)}")

Quiz(BankSoal)