#################################
# @Author: Pascal A. d'ALMEIDA  #
#################################
from ortools.sat.python import cp_model
from ortools.linear_solver import pywraplp


class VarArraySolutionPrinterWithLimit(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables, limit):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0
        self.__solution_limit = limit

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s=%i' % (v, self.Value(v)), end=' ')
        print()
        if self.__solution_count >= self.__solution_limit:
            print('Stop search after %i solutions' % self.__solution_limit)
            self.StopSearch()

    def solution_count(self):
        return self.__solution_count


model = cp_model.CpModel()



## Create SOLVER

solver = pywraplp.Solver.CreateSolver('SCIP')

####################################################### Exercice 1##########################
#Une petite aciérie(usine de fabrication d'acier) doit décider de l’allocation pour la     #
#semaine prochaine (40 heures au total) de son laminoir(machine utilisée pour              #
#reduire l'epaisseur des matières). Celui-ci traite des plaques d’acier non finies et      #
#peut produire deux types de produits semi-finis, des bandes et des rouleaux. Le           #
#laminoir peut produire 200 bandes ou 140 rouleaux par heure, sachant qu’une bande         #
#rapporte $ 25 et un rouleau $ 30. Enfin, il ne faut pas produire davantage que le total   #
#des commandes programmées, à savoir 6000 bandes et 4000 rouleaux.                         #
#Déterminer les quantités respectives à produire pour maximiser le profit.                 #
####################################################### Exercice 1##########################

x = solver.IntVar(1, 100, 'x')
y = solver.IntVar(1, 100, 'y')
z = solver.IntVar(1, 100, 'z')

solver.Add(x + y + z == 100)
solver.Add((0.5 * x) + (5 * y) + (10 * z) == 100)

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("------------------------------------------------------------------")
    print('Solution exercice 1:')
    print('x =', x.solution_value())
    print('y =', y.solution_value())
    print('z =', z.solution_value())
    print("------------------------------------------------------------------")


else:
    print('TPas de solution optimal')





####################################################   EXERCICE 2   ##############################
#   Un fermier envoie son fils au marché avec 100$. Avec ce 100$, le fils doit acheter cent      #
#   animaux. Il doit revenir à la ferme avec les 100 animaux et il lui faut dépenser les 100$ au #
#   complet. Un poussin coûte 0.50$, un cochon 5$ et un boeuf 10$. Le fils doit acheter au       #
#   moins un animal de chaque espèce.                                                            #
#   Combien le fils aura-t-il de poussins, de cochons et de boeufs ?                             #
##################################################################################################

e2 = input("Entrer le nombre maximal de pièces de 200f:\n")
e1 = input("Entrer le nombre maximal de pièces de 100f:\n")
c50 = input("Entrer le nombre maximal de pièces de 50f:\n")
c25 = input("Entrer le nombre maximal de pièces de 25f:\n")
c10 = input("Entrer le nombre maximal de pièces de 10f:\n")
T = input("Entrer le nombre total de pièces:\n")
P = input("Entrer le prix de la boisson:\n")
x = solver.IntVar(0, int(e2), 'x')
y = solver.IntVar(0, int(e1), 'y')
z = solver.IntVar(0, int(c50), 'z')
t = solver.IntVar(0, int(c25), 't')
k = solver.IntVar(0, int(c10), 'k')



solver.Add(200 * x + 100 * y + 50 * z + 25 * t + 10 * k == int(T) - int(P))

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("------------------------------------------------------------------")
    print('Solution exercice 2:')
    print('x =', x.solution_value())
    print('y =', y.solution_value())
    print('z =', z.solution_value())
    print('t =', t.solution_value())
    print('k =', k.solution_value())
    print("------------------------------------------------------------------")

else:
    print('The problem does not have an optimal solution.')


#################################################  EXERCICE  3   ###################################
#   On s’intéresse à un distributeur automatique de boissons.                                      #
#   L’utilisateur insère des pièces de monnaie pour un total de T fcfa, puis il sélectionne une    #
#   boisson, dont le prix est de P fcfa. Il faut calculer la monnaie à rendre, sachant que le      #
#   distributeur a en réserve E2 pièces de 200f, E1 pièces de 100f, C50 pièces de 50f, C25         #
#   pièces de 25f et C10 pièces de 10f.                                                            #
#   Que faut-il ajouter si on veut minimiser le nombre de pièces à rendre.                         #
##################################################################################################



# x le nombre de bandes 
# y le nombre de rouleaux 


x = solver.IntVar(0, 6000, 'x')
y = solver.IntVar(0, 4000, 'y')

solver.Add((1 / 200) * x + (1 / 140) * y <= 40)

solver.Maximize(25 * x + 30 * y)

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print("------------------------------------------------------------------")
    print('Solution exercice 3:')
    print('x =', x.solution_value())
    print('y =', y.solution_value())
    print("------------------------------------------------------------------")
else:
    print('Pas de solution optimal.')

