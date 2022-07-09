# 🎰 Máquina de estados

### 📉 Diagrama de estados

<p align=center><img width="300" src="https://github.com/DianaIT/tfg/blob/master/docs/maquinaEstados.png" /></p>

## 🌟 Estados

### 👋 Grettings

- Recibe el nombre del paciente, el número de preguntas a realizar en el ejercicio de emociones y la dificultad del ejercicio de orientacion.
- Saluda al niño y empieza con el primer ejercicio

---

     💬 Hola Amelia, soy Jinko, Vamos a empezar
         ➡️ EMOTION

### ❤️ Emotion

- Rrecupera las preguntas y sus respuestas de la base de datos
- Empieza a preguntar al niñp

---

    ¿Todas las preguntas realizadas? ➡️ ORIENTATION
     💬 PREGUNTA
        Acierto  Pasa a la siguiente pregunta  ➡️ EMOTION
        Fallo 💬 Repite más despacio  ➡️ EMOTION

### ⤴️ Orientation

- El robot que le pide al paciente que se prepare y que le siga. Existen dos dificultades para est ejercicio:

- Facil ➡️ Trayectoria en linea recta
- Intermedio ➡️ Trayectoria en zig zag

---

    💬  Muy bien, ahora quiero que me sigas, ¿Preparada?

### 📚 Results

- Guarda los datos en la BBDD
- Se despide del niño
