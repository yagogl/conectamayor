================================================================================
  MEMORIA TFG — CONECTAMAYOR — Yago Gamo López
  GUÍA DE INSTALACIÓN Y COMPILACIÓN (VS Code en Ubuntu)
================================================================================

Sigue los pasos en orden. Tardarás unos 15 minutos la primera vez (la mayor
parte la ocupa la instalación de TeX Live).

--------------------------------------------------------------------------------
PASO 1 — Instalar TeX Live (LaTeX) y latexmk
--------------------------------------------------------------------------------

Abre una terminal y ejecuta:

    sudo apt update
    sudo apt install texlive-full latexmk

Sí, son ~5 GB. Es lo más cómodo: instala todo lo que la plantilla puede
necesitar y te ahorras perseguir paquetes faltantes uno a uno.


--------------------------------------------------------------------------------
PASO 2 — Instalar la extensión "LaTeX Workshop" en VS Code
--------------------------------------------------------------------------------

  1. Abre VS Code
  2. Ve al panel de Extensiones (Ctrl+Shift+X)
  3. Busca: "LaTeX Workshop"
  4. Instala la que tiene como autor a "James Yu"

Esa es la extensión estándar para LaTeX en VS Code. Te da:
  - Compilación con un atajo (Ctrl+Alt+B)
  - Vista previa del PDF al lado del código (Ctrl+Alt+V)
  - Autocompletado de comandos LaTeX
  - Resaltado de errores


--------------------------------------------------------------------------------
PASO 3 — Preparar la carpeta de trabajo
--------------------------------------------------------------------------------

3.1) Crea una carpeta limpia para tu memoria. Por ejemplo:

         ~/Documentos/TFG/memoria/

3.2) Descomprime DENTRO de esa carpeta el ZIP de Moodle
     ("plantilla-latex-para-tfx-tesis-master.zip"). Te quedará algo así:

         memoria/
         ├── tfgtfmthesisuam.cls
         ├── tfgtfmthesisuam.ist
         ├── tfgtfmthesisuam.tex     <-- ESTO ES EL MANUAL DE EJEMPLO, NO LA MEMORIA
         ├── (varios archivos .sty, .bst, ...)
         └── (carpetas estetica/, estructura/, primpas/, elemint/, varios/, img/)

3.3) RENOMBRA el archivo del manual para que no estorbe:

         mv tfgtfmthesisuam.tex manual_plantilla.tex

3.4) Descomprime AHORA mi ZIP ("memoria_conectamayor.zip") TAMBIÉN dentro
     de la misma carpeta `memoria/`. Es decir, los archivos que yo te doy
     se mezclan con los de la plantilla. Cuando pregunte si quieres
     sobrescribir algo, di que sí (puede haber alguna carpeta `img/` que
     coincida; la que yo te paso está vacía, no se pierde nada).

3.5) El resultado final debería ser:

         memoria/
         ├── tfgtfmthesisuam.cls         (de la plantilla — NO TOCAR)
         ├── tfgtfmthesisuam.ist         (de la plantilla — NO TOCAR)
         ├── (otros .sty, .bst, etc.)    (de la plantilla — NO TOCAR)
         ├── manual_plantilla.tex        (el manual renombrado — IGNORAR)
         ├── estetica/, estructura/, …   (carpetas del manual — IGNORAR)
         │
         ├── memoria.tex                 ← EL FICHERO QUE COMPILAS
         ├── memoria.bib                 ← bibliografía
         ├── README.txt                  ← este archivo
         ├── .vscode/
         │   └── settings.json           ← configuración para VS Code
         ├── inicio/
         │   ├── prefacio.tex
         │   ├── agradecimientos.tex
         │   ├── resumen.tex
         │   └── abstract.tex
         ├── capitulos/
         │   └── introduccion.tex        ← Capítulo 1 (entregado)
         ├── apendices/                  (vacía por ahora)
         ├── img/                        (capturas de pantalla, vacía)
         ├── codes/                      (fragmentos de código, vacía)
         └── data/                       (datos numéricos, vacía)


--------------------------------------------------------------------------------
PASO 4 — Abrir el proyecto en VS Code
--------------------------------------------------------------------------------

Desde la terminal, dentro de la carpeta `memoria/`:

    code .

(o desde VS Code: Archivo → Abrir carpeta → seleccionar `memoria/`)

Es importante que abras la CARPETA, no un archivo suelto. La extensión
LaTeX Workshop necesita ver todo el proyecto para poder resolver los
ficheros que se incluyen unos a otros.

VS Code leerá automáticamente la configuración del archivo
`.vscode/settings.json` que viene en mi ZIP. Esa configuración le dice
a LaTeX Workshop:
  - cómo compilar el proyecto (pdflatex → bibtex → pdflatex → pdflatex)
  - qué archivos limpiar después de compilar
  - dónde mostrar el PDF


--------------------------------------------------------------------------------
PASO 5 — Compilar la memoria
--------------------------------------------------------------------------------

5.1) Abre `memoria.tex` en VS Code (haz clic en él en el explorador de
     archivos de la izquierda).

5.2) Pulsa Ctrl+Alt+B   →   esto inicia la compilación.

     Verás abajo a la izquierda una notificación: "LaTeX compiling…"
     Tarda entre 30 segundos y 2 minutos la primera vez.

5.3) Si todo va bien, verás el mensaje "Build succeeded".
     Se habrá generado el archivo `memoria.pdf` en la misma carpeta.

5.4) Para ver el PDF: pulsa Ctrl+Alt+V. Se abrirá en una pestaña al lado.


--------------------------------------------------------------------------------
PASO 6 — Si falla la compilación
--------------------------------------------------------------------------------

Pasos a hacer EN ORDEN:

a) Mira el panel "PROBLEMS" de VS Code (Ctrl+Shift+M). Allí aparecen los
   errores con número de línea y archivo.

b) Mira el panel de salida de LaTeX Workshop:
   View → Output → en el desplegable arriba, elige "LaTeX Compiler"

c) Errores típicos y solución:

   • "Package XXX not found"
     → Falta un paquete LaTeX. Instala texlive-full si no lo hiciste.

   • "File `tfgtfmthesisuam.cls' not found"
     → No están los archivos de la plantilla. Vuelve al PASO 3 y
       asegúrate de descomprimir el ZIP de Moodle EN LA MISMA CARPETA.

   • Errores de sintaxis raros con `\chapter{...}{ruta}`
     → Cópiame el mensaje exacto del error y lo miramos juntos. Esa
       sintaxis es propia de la clase EPS-UAM y a veces hay sutilezas.

d) Si nada de lo anterior funciona, copia los ÚLTIMOS 30-40 líneas del
   panel de salida y mándamelas en el chat. La mayor parte de las veces
   el error exacto está ahí.


--------------------------------------------------------------------------------
PASO 7 — Antes de seguir con el siguiente capítulo
--------------------------------------------------------------------------------

Una vez que hayas conseguido compilar y veas el PDF:

  1. Léete el Capítulo 1 (Introducción) entero, despacio.

  2. Si hay frases que no te suenan a ti, cámbialas en
     `capitulos/introduccion.tex`. La voz tiene que ser tuya.

  3. En `memoria.bib`, cambia los "[INDICAR FECHA EN QUE LO CONSULTASTE]"
     por la fecha real en que viste cada página. Pilar fue muy explícita
     con eso.

  4. Personaliza `inicio/agradecimientos.tex` si quieres añadir o quitar
     a alguien.

  5. Avísame en el chat y arrancamos con el Capítulo 2 (Estado del arte).


--------------------------------------------------------------------------------
ATAJOS ÚTILES EN VS CODE
--------------------------------------------------------------------------------

  Ctrl + Alt + B    Compilar (build)
  Ctrl + Alt + V    Ver el PDF al lado
  Ctrl + Alt + J    Saltar entre código y posición en el PDF (SyncTeX)
  Ctrl + Shift + P  Paleta de comandos (busca "LaTeX" para ver todo lo
                    que la extensión puede hacer)


================================================================================
  FIN DE LA GUÍA
================================================================================
