using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static Practica2_Estructura.estudiantes;

namespace Practica2_Estructura
{
    internal class Grupo_Estudiante
    {
        public class grupo_Estudiante
        {
            // Atributos
            public string NombreGrupo { get; set; }
            public string ClaveGrupo { get; set; }
            public Estudiante[] Estudiantes { get; set; }

            // Constructor
            public grupo_Estudiante(string nombreGrupo, string claveGrupo, Estudiante[] estudiantes)
            {
                NombreGrupo = nombreGrupo;
                ClaveGrupo = claveGrupo;
                Estudiantes = estudiantes;
            }

            // Promedio del grupo
            public double PromedioGrupo()
            {
                if (Estudiantes.Length == 0)
                {
                    return 0;
                }

                double suma = 0;

                foreach (Estudiante estudiante in Estudiantes)
                {
                    suma += estudiante.Promedio();
                }

                return suma / Estudiantes.Length;
            }

            // Estudiantes regulares
            public Estudiante[] EstudiantesRegulares()
            {
                List<Estudiante> regulares = new List<Estudiante>();

                foreach (Estudiante estudiante in Estudiantes)
                {
                    if (estudiante.Promedio() >= 70)
                    {
                        regulares.Add(estudiante);
                    }
                }

                return regulares.ToArray();
            }

            // Estudiantes irregulares
            public Estudiante[] EstudiantesIrregulares()
            {
                List<Estudiante> irregulares = new List<Estudiante>();

                foreach (Estudiante estudiante in Estudiantes)
                {
                    if (estudiante.Promedio() < 70)
                    {
                        irregulares.Add(estudiante);
                    }
                }

                return irregulares.ToArray();
            }
        }
    }
}
