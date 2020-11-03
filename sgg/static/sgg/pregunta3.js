const filas = 10
const columnas = 10
const valor_1_fila = ["$2.000","$3.300","$5.000","$7.100","$10.000","$14.000","$20.000","$30.000","$50.000","$110.000"]
const valor_2_fila = "$0"
const images = ["1tBaOrudcIjpM5Q3XUKRO5Dk3RZYuyIxv", "1Sj0FaIS0_P4Z8xFQD2Xrel30yC55gu1V", "1iDOh8bOxmJJgh-d-tckCm_ELi-iJ7gSx", "1DkrOzluxssRHq8RZ7BbRgkqUf1p9tPiW",
                "18rw4DWQtHKBU6dJfLpsaGUMsjbdsYnyY", "1nLgdhbVGcfG6o-0VAY5_B4t4_2EuNdM3", "19qxHB25ZKsZDAu_1zcBF2GzHXbd0AG7x", "19IKbxIIwbsoiuZjEOSUkuqyf5D9l3dFs",
                "15-c4SPMFjo_Zuo6EOTG_MCarIWdplJO4", "1h4aZZ8WVo5s_lB8Fp59Xh334aNAVIo9Y"
              ];
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
  col2.innerHTML = '<input class="radio" data-toggle="modal" data-target="#staticBackdrop" onclick="clickaction()" type="radio" name="sgg_p3" value="'+(j+1)+'">';
  var col3 = document.createElement("td")
  col3.classList.add("align-middle");
  col3.innerHTML = "<img width='100px' src='https://drive.google.com/uc?id="+images[j]+"' />";
  col3.setAttribute("id", "divcircles")
  // col4.classList.add("col-5", "div-circles");

  fila.appendChild(col1)
  fila.appendChild(col3)
  fila.appendChild(col2)

  // fila.appendChild(col4)
  contenido.appendChild(fila)

}