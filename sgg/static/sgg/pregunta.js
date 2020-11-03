const filas = 10
const columnas = 10
const valor_1_fila = ["$2.000","$2.200","$2.600","$2.900","$3.500","$4.200","$5.300","$7.100","$10.800", "$21.800"]
const valor_2_fila = "$0"
contenido = document.getElementById("contenido");
const images = ["1tBaOrudcIjpM5Q3XUKRO5Dk3RZYuyIxv", "1O2auAxERAEtlqBk92d4LhNBjYum3OWdK", "1bNs1elsuacqU5XDLL7T7XGoytIyN0lbV", "1_dRmuB_0jMhWgfxGf6ayQ249hsdIc-Nu",
                "1KxBu_YwX_O3XSGqTAMJ2JqPQBg9CBg5h", "1NmuFnJ9Sb2Eb--BJM0iFFP06wCtyLNk-", "1hyndQr5mKqZF23dXEHMhZGZ6HnoVwDhD", "1ANaDeKbA4PZYKpNIU5bZJsKhFsIK4iAB",
                "17j2TTTHFMMJhFXrbWPvWRLqHLSzkq8j2", "18BY1vWeZQjKynw5fMZ35JAQuH_rQm7TW"
              ];
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
  col2.innerHTML = '<input class="radio" data-toggle="modal" data-target="#staticBackdrop" onclick="clickaction()" type="radio" name="sgg_p1" value="'+(j+1)+'">';
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