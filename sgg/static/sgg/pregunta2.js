const filas = 10
const columnas = 10
const valor_1_fila = ["$2.000","$2.400","$3.000","$3.700","$4.700","$6.000","$8.000","$11.300","$18.000","$38.000"]
const valor_2_fila = "$0"
const images = ["1tBaOrudcIjpM5Q3XUKRO5Dk3RZYuyIxv", "1r1rqzbKj5IPqFvM2XqCZbM_wJAx_vtIa", "1j1b9vtq1qm_fsOF0fMTfDiFP8XumejHc", "1CZTEVkhXEVxK_IIi2nQZFfKdf-l-U_FD",
                "1FJuTTjHSVpLLqfE2N3u7M-EHEHmKaVzr", "1-aoI8g9lrwYB-7At_9R5yOYZath5aRRH", "160enBSxh6SK9amq7I2uW-I2u1P_d7MWN", "1ZYWHr3QlSlRUJQK_KuuO_rm5xJl9phiV",
                "1BCPSNdKNaWvp_85t83MqXHz_uUoAfkTt", "1K1G3lz2pFhq7oUect8BzQ1-S1BxZqc3-"
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
  col2.innerHTML = '<input class="radio" data-toggle="modal" data-target="#staticBackdrop" onclick="clickaction()" type="radio" name="sgg_p2" value="'+(j+1)+'">';
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