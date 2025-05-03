
Šiame projekte yra įgivendintas Sudoku sprendinklis, naudojant objektinio programavimo principus Python kalba.

Funkcionalumai:
    
    9x9 Sudoku galvosūkio sprendimas;
    Galimybė įrašyti / įkelti lentas iš failų;
    Konsolės pagrindu veikianti demonstracija;

    # Paleisti sprendiklį 
    python sudoku_solver.py

    # Paleisti vienetinius testus 
    python test_sudoku.py

Projekto struktūra:
    
    sudoku_solver.py - sprendimo logika naudojant atgalinio paieškos algoritmą ir Singelton dizaino modelį;

    sudoku_board.py - lentelės valdymo klasė su dailų nuskaitymu arba išrašymu;

    test_sudoku.py - vienetiniai testai Sudoku lenteles funkcionalumui tikrinti.

Naudoti OPP principai:
    
    Inkapsuliacija - kiekviena klasė turi savo duomenis ir metodus pavyzdžiui SudokuBoard.Board;

    Abstrakcija - abstrakti bazinė klasė Board Base apibrėžia sąsajas failų įrašymui arba nuskaitymui;

    Paveldėjimas - SudokuBoard paveldi iš BoardBase ir įgivendina jos metodus;

    Polimorfizmas - SudokuBoard perrašo abstrakčius metodus savo konkrečiu įgivendinimu.

Naudotas dizaino modelis - Singelton.
    
    SudokuSolver klasė naudoja Singelton modelį. Tai užtikrina, kad per visą programą veiktų tik viena SudokuSolver klasės instankcija.

Kompozicija / Agregacija
   
    Šioje programoje buvo naudojama Kompozicija.
    SudokuSolver turi SudokuBoard egzempliorių galvosūkio valdymui.

    Ši priklausomybė apibrėžia glaudų objektų ryšį ir leidžia aiškiai susieti funkcijas.

Failų nuskaitymas / išrašymas
    
    Lentelę galima išsaugoti, įkelti taip:
    
    board.save_to_file("file.txt")
    board.load_from_file("file.txt")

    Formatavimas: 9 eilutės skaičių, atskirtų tarpais, 0 reikšmė reiškia tuščią langelį.

Testavimas:
   
    Testai pateikti test_sudoku.py faile, naudojant unittest modulį:

    def test_board_initialization(self):
    self.assertEqual(len(self.board.board), 9)

    Padengiami: lentelės dydis ir reikšmės, reikšmių priskyrimo testai.

Rezultatai:
    
    Sprendžiamos kelios sudoku užduotys;
    Įgivendinti visi 4 OPP principai;
    Naudotas Singelton modelis;
    Veikia failų įvestis, išvestis, testai;
    Sunkumai buvo struktūrizuojant paveldėjimą ir užtikrinant tinkamą klasių sąsają bei funkcionalumą.

Išvados:
   
    Projektas parodo OPP pritaikymą Python kalboje;
    Sudoku galvosūkiai sprendžiami teisingai, laikantis gerosios kodo praktikos.

Galimybės plėtrai:
    
    Grafinė sąsaja;
    Sunkumo lygių parinkimas;
    Automatinis užduočių generavimas.