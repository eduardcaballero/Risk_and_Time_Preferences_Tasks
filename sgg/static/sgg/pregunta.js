const filas = 10
const columnas = 10
const valor1 = "$26.000"
const valor2 = "$21.000"
const valor3 = "$50.000"
const valor4 = "$1.000"
contenido = document.getElementById("contenido");

for (var j = 0; j < filas; j++) {
  var row = document.createElement("div");
  var row2 = document.createElement("div");

  for (var i = 0; i < columnas; i++) {
    var circle = document.createElement("span");
    var circle2 = document.createElement("span");
    if (i < j) {
      circle.classList.add("dot", "color1");
      circle.innerText = valor2;
      circle2.classList.add("dot", "color1");
      circle2.innerText = valor4;
    } else {
      circle.classList.add("dot", "color2");
      circle.innerText = valor1;
      circle2.classList.add("dot", "color2");
      circle2.innerText = valor3
    }
    row.appendChild(circle);
    row.classList.add("div-circles")
    row2.appendChild(circle2);
    row2.classList.add("div-circles")
  }
  var fila = document.createElement("tr")
  var col1 = document.createElement("td")
  // col1.classList.add("col-5", "div-circles");
  col1.appendChild(row);
  var col2 = document.createElement("td")
  col2.classList.add("align-middle");
  col2.innerHTML = '<input class="radio" type="radio" name="sgg_p1" value="A">';
  var col3 = document.createElement("td")
  col3.classList.add("align-middle");
  col3.innerHTML = "<img width='100px' src='https://drive.google.com/uc?id=1lU9CNMJouxKbvEwdxPJuTzSKkZh5jPER' />";
  col3.setAttribute("id", "divcircles")
  var col4 = document.createElement("td")
  // col4.classList.add("col-5", "div-circles");
  col4.appendChild(row2);

  fila.appendChild(col1)
  fila.appendChild(col3)
  fila.appendChild(col2)

  // fila.appendChild(col4)
  contenido.appendChild(fila)

}