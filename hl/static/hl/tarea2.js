const filas = 10
const columnas = 10
const valor1 = "$35.000"
const valor2 = "$14.000"
const valor3 = "$63.000"
const valor4 = "$1.000"
contenido = document.getElementById("contenido");

for (var j = 0; j < filas; j++) {
  var row = document.createElement("div");
  var row2 = document.createElement("div");

  for (var i = 0; i < columnas; i++) {
    var circle = document.createElement("span");
    var circle2 = document.createElement("span");
    if (i <= j) {
      circle.classList.add("dot", "color2");
      circle.innerText = valor1;
      circle2.classList.add("dot", "color2");
      circle2.innerText = valor3
    } else {
      circle.classList.add("dot", "color1");
      circle.innerText = valor2;
      circle2.classList.add("dot", "color1");
      circle2.innerText = valor4;
    }
    circle.setAttribute("data-toggle", "tooltip");
    row.appendChild(circle);
    row.classList.add("div-circles")
    circle2.setAttribute("data-toggle", "tooltip");
    row2.appendChild(circle2);
    row2.classList.add("div-circles")
  }
  var fila = document.createElement("tr")
  var col1 = document.createElement("td")
  // col1.classList.add("col-5", "div-circles");
  col1.appendChild(row);
  var col2 = document.createElement("td")
  col2.classList.add("align-middle");
  col2.innerHTML = '<input class="radio" data-toggle="modal" data-target="#staticBackdrop" onclick="clickaction()" type="radio" name="hl_t2_p' + (j+1) + '" value="A">';
  var col3 = document.createElement("td")
  col3.classList.add("align-middle");
  col3.innerHTML = '<input class="radio" data-toggle="modal" data-target="#staticBackdrop" onclick="clickaction()" type="radio" name="hl_t2_p' + (j+1) + '" value="B">';
  col3.setAttribute("id", "divcircles")
  var col4 = document.createElement("td")
  // col4.classList.add("col-5", "div-circles");
  col4.appendChild(row2);
  fila.appendChild(col1)
  fila.appendChild(col2)
  fila.appendChild(col3)
  fila.appendChild(col4)
  contenido.appendChild(fila)

}

// $('.div-circles [data-toggle="tooltip"]').tooltip({
//   animated: 'fade',
//   html: true
// });

// function submit(ev) {
//   var formData = new FormData(document.forms.namedItem("elecciones"));
//   var html = "A continuación, se presenta un resumen de su elección por fila y sus posibles ganancias si esa fila es seleccionada para el pago: <br><ol>"
//   var count = 0
//   for (var pair of formData.entries()) {
//     count++
//     var pago1 = ""
//     var pago2 = ""
//     let index = parseInt(pair[1][1])
//     if (pair[1][0] == "A") {
//       pago1 = "$26.000"
//       pago2 = "$21.000"
//     } else {
//       pago1 = "$50.000"
//       pago2 = "$1.000"
//     }
//     html += "<li>Ha seleccionado la opción " + pair[1][0] + ". Es decir, si la fila " + (index + 1) +
//       " sale seleccionada para el pago, usted recibe: <br><ul><li>" +
//       pago1 + " si sale la pelota azul ( " + ((parseInt(index) + 1) * 10) + "% de probabilidad ) </li><li>" +
//       pago2 + " si sale la pelota blanca ( " + (100 - (parseInt(index) + 1) * 10) + "% de probabilidad )</li></ul></li>"
//   }
//   html += "</ol>"
//   var title = document.getElementById("modalRadioButtonLabel")
//   var buttonClose = document.getElementById("modalRadioButtonClose")
//   var buttonConfirm = document.getElementById("modalRadioButtonConfirm")
//   if (count == 10) {
//     title.innerHTML = "¿Está seguro de sus elecciones?"
//     buttonClose.style.visibility = "visible"
//     buttonConfirm.innerHTML = "Si"
//     document.getElementById("mensaje").innerHTML = html
//   } else {
//     title.innerHTML = "Información"
//     buttonClose.style.visibility = "hidden"
//     buttonConfirm.innerHTML = "Ok"
//     document.getElementById("mensaje").innerHTML = "Debe completar todas las respuestas, faltan " + (10 - count) + " respuestas."
//     $('#modalRadioButton').modal(true)
//   }
// }