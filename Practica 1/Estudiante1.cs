using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practica_1
{
    internal class Estudiante1
    {
        string Nombre;
        string Carrera;
        int[] calificaciones;

        public Estudiante1(string nombre, string carrera, int num_calif)
        {
          this.Nombre = nombre;
          this. Carrera = carrera ; 
          this.calificaciones = new int[num_calif];
            }
    public void CapturaCalificacion (int materia, int calif)
        {
            calificaciones[materia] = calif;
        }
        public int getPromedio()
        {
            int suma = 0;
            int promedio = 0;
            for (int i = 0; i < calificaciones.Length; i++)
            {
                suma += calificaciones[i];
            }
            promedio = suma / calificaciones.Length;
            return promedio;
        }
        public bool Esregular()
        {
            for(int i = 0; i < calificaciones.Length; i++)
            {
                if (calificaciones[i] < 70)
                {
                    return false ; 
                }
            }
            return true;
        }

     } // envair invitacion al profe mario en la aplicasion de git, y subir el proyecto de esta practica al repositorio
 }


