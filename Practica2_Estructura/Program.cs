using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;



namespace Practica2_Estructura
{
    internal class Program
    {
        static void Main(string[] args)
        {
            estudiantes.Estudiante[] grupo =
                new estudiantes.Estudiante[0];

            int opcion;

            do
            {
                Console.Clear();

               
                Console.WriteLine(" GRUPO DE ESTUDIANTES");
               
                Console.WriteLine("1. AGREGAR UN ESTUDIANTE");
                Console.WriteLine("2. CONSULTAR ESTUDIANTES");
                Console.WriteLine("3. CONSULTAR PROMEDIO DEL GRUPO");
                Console.WriteLine("4. MOSTRAR ESTUDIANTES REGULARES");
                Console.WriteLine("5. MOSTRAR ESTUDIANTES IRREGULARES");
                Console.WriteLine("6. SALIR");
              
                Console.Write("Opcion: ");

                opcion = Convert.ToInt32(Console.ReadLine());
                //MODIFICASION DE LA PRACTICA 5 
                switch (opcion)
                {
                    case 1:
                        {
                            Console.Clear();

                            Console.WriteLine(" AGREGAR ESTUDIANTE ");

                            Console.Write("Nombre: ");
                            string nombre = Console.ReadLine();

                            Console.Write("Carrera: ");
                            string carrera = Console.ReadLine();

                            Console.Write("Numero de materias: ");
                            int numMaterias =
                                Convert.ToInt32(Console.ReadLine());

                            estudiantes.Estudiante nuevo =
                                new estudiantes.Estudiante(
                                    nombre,
                                    carrera,
                                    numMaterias
                                );

                            for (int i = 0; i < numMaterias; i++)
                            {
                                Console.Write(
                                    "Calificacion de la materia "
                                    + (i + 1) + ": "
                                );

                                int calificacion =
                                    Convert.ToInt32(Console.ReadLine());

                                nuevo.CapturaCalificacion(
                                    i,
                                    calificacion
                                );
                            }

                            estudiantes.Estudiante[] nuevoGrupo =
                                new estudiantes.Estudiante[
                                    grupo.Length + 1
                                ];

                            for (int i = 0; i < grupo.Length; i++)
                            {
                                nuevoGrupo[i] = grupo[i];
                            }

                            nuevoGrupo[nuevoGrupo.Length - 1] = nuevo;

                            grupo = nuevoGrupo;

                            Console.WriteLine();
                            Console.WriteLine(
                                "Estudiante agregado correctamente."
                            );

                            Console.WriteLine();
                            Console.WriteLine(
                                "Presiona enter para continuar..."
                            );
                            Console.ReadLine();

                            break;
                        }

                    case 2:
                        {
                            Console.Clear();

                            Console.WriteLine(
                                "** DATOS DEL GRUPO **"
                            );
                            Console.WriteLine();

                            if (grupo.Length == 0)
                            {
                                Console.WriteLine(
                                    "No hay estudiantes registrados."
                                );
                            }
                            else
                            {
                                for (int i = 0; i < grupo.Length; i++)
                                {
                                    Console.WriteLine(
                                        "ESTUDIANTE #" + (i + 1)
                                    );

                                    Console.WriteLine(
                                        "Promedio: "
                                        + grupo[i].getPromedio()
                                    );

                                    Console.WriteLine(
                                        "Estatus: "
                                        + (grupo[i].Esregular()
                                            ? "REGULAR"
                                            : "IRREGULAR")
                                    );

                                    Console.WriteLine(
                                        "----------------------------"
                                    );
                                }
                            }

                            Console.WriteLine();
                            Console.WriteLine(
                                "Presiona ENTER para continuar..."
                            );
                            Console.ReadLine();

                            break;
                        }

                    case 3:
                        {
                            Console.Clear();

                            Console.WriteLine(
                                "** PROMEDIO DEL GRUPO **"
                            );

                            if (grupo.Length == 0)
                            {
                                Console.WriteLine(
                                    "No hay estudiantes registrados."
                                );
                            }
                            else
                            {
                                double suma = 0;

                                for (int i = 0; i < grupo.Length; i++)
                                {
                                    suma += grupo[i].getPromedio();
                                }

                                double promedio =
                                    suma / grupo.Length;

                                Console.WriteLine(
                                    "Promedio del grupo: "
                                    + promedio.ToString("0.00")
                                );
                            }

                            Console.WriteLine();
                            Console.WriteLine(
                                "Presiona ENTER para continuar..."
                            );
                            Console.ReadLine();

                            break;
                        }

                    case 4:
                        {
                            Console.Clear();

                            Console.WriteLine(
                                "** ESTUDIANTES REGULARES **"
                            );
                            Console.WriteLine();

                            bool encontrados = false;

                            for (int i = 0; i < grupo.Length; i++)
                            {
                                if (grupo[i].Esregular())
                                {
                                    Console.WriteLine(
                                        "Estudiante #" + (i + 1)
                                    );

                                    Console.WriteLine(
                                        "Promedio: "
                                        + grupo[i].getPromedio()
                                    );

                                    Console.WriteLine(
                                        "----------------------------"
                                    );

                                    encontrados = true;
                                }
                            }

                            if (!encontrados)
                            {
                                Console.WriteLine(
                                    "No hay estudiantes regulares."
                                );
                            }

                            Console.WriteLine();
                            Console.WriteLine(
                                "Presiona ENTER para continuar..."
                            );
                            Console.ReadLine();

                            break;
                        }

                    case 5:
                        {
                            Console.Clear();

                            Console.WriteLine(
                                "** ESTUDIANTES IRREGULARES **"
                            );
                            Console.WriteLine();

                            bool encontrados = false;

                            for (int i = 0; i < grupo.Length; i++)
                            {
                                if (!grupo[i].Esregular())
                                {
                                    Console.WriteLine(
                                        "Estudiante #" + (i + 1)
                                    );

                                    Console.WriteLine(
                                        "Promedio: "
                                        + grupo[i].getPromedio()
                                    );

                                    Console.WriteLine(
                                        "----------------------------"
                                    );

                                    encontrados = true;
                                }
                            }

                            if (!encontrados)
                            {
                                Console.WriteLine(
                                    "No hay estudiantes irregulares."
                                );
                            }

                            Console.WriteLine();
                            Console.WriteLine(
                                "Presiona ENTER para continuar..."
                            );
                            Console.ReadLine();

                            break;
                        }

                    case 6:
                        Console.WriteLine(
                            "Programa terminado."
                        );
                        break;

                    default:
                        Console.WriteLine(
                            "Opcion no valida."
                        );

                        Console.WriteLine(
                            "Presiona ENTER para continuar..."
                        );
                        Console.ReadLine();

                        break;
                }

            } while (opcion != 6);
        }
    }
}