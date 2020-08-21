const filas = 10
const columnas = 10
const valor_1_fila = ["$2.000","$2.400","$3.000","$3.700","$4.700","$6.000","$8.000","$11.300","$18.000","$38.000"]
const valor_2_fila = "$0"

contenido = document.getElementById("contenido");

for (var j = 0; j < filas; j++) {
  var row = document.createElement("div");

  for (var i = 0; i < columnas; i++) {
    var circle = document.createElement("span");
    if (i < j) {
      circle.classList.add("dot", "color1");
      circle.innerText = valor_2_fila;
    } else {
      circle.classList.add("dot", "color2");
      circle.innerText = valor_1_fila[j];
    }
    row.appendChild(circle);
    row.classList.add("div-circles")
  }
  var fila = document.createElement("tr")
  var col1 = document.createElement("td")
  // col1.classList.add("col-5", "div-circles");
  col1.appendChild(row);
  var col2 = document.createElement("td")
  col2.classList.add("align-middle");
  col2.innerHTML = '<input class="radio" type="radio" name="sgg_p2" value="'+(j+1)+'">';
  var col3 = document.createElement("td")
  col3.classList.add("align-middle");
  col3.innerHTML = "<img width='100px' src='https://drive.google.com/uc?id=1lU9CNMJouxKbvEwdxPJuTzSKkZh5jPER' />";
  col3.setAttribute("id", "divcircles")
  // col4.classList.add("col-5", "div-circles");

  fila.appendChild(col1)
  fila.appendChild(col3)
  fila.appendChild(col2)

  // fila.appendChild(col4)
  contenido.appendChild(fila)

}