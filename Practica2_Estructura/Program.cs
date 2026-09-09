using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace practica1._0
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int opcion = 0;
                Console.WriteLine("SELECCIONA UNA OPCION ");
                Console.WriteLine("1- AGREGAR UN ESTUDIANTE");
                Console.WriteLine("2- CONSULTAR EL ESTUDIANTE");
                Console.WriteLine("3- SALIR");

                Console.Write("opcion: ");
            opcion = Convert.ToInt32(Console.ReadLine());

            switch (opcion)
            {
                case 1: capturarEstudiante();
                    break;
                        }
        

            Console.ReadLine();
            }
        static estudiante capturarEstudiante()
        {
            //aqui piden el nombre y la carrera 
            string nombre, carrera;
            int num_materias;
           
            Console.WriteLine("introduce tu nombre: " );
            nombre = Console.ReadLine();
            
            Console.WriteLine("introduce tu carrera: ");
            carrera = Console.ReadLine();

            Console.WriteLine("introduce numero de materias: ");
            num_materias = Convert.ToInt32(Console.ReadLine());


            //creamos un objeto de tipo estudiante 
            estudiante estudiante_nuevo = new estudiante(nombre, carrera, num_materias);
            int calificacion = 0;
            for (int i = 0; i < num_materias;  i ++)
            {
                Console.WriteLine("calificacion de la materia" + (i + 1));
                calificacion = Convert.ToInt32(Console.ReadLine());

                estudiante_nuevo.CapturaCalificacion(i, calificacion);

            }

            

            return estudiante_nuevo;

        }
        }
    }

