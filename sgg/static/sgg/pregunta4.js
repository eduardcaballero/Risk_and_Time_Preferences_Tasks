const filas = 10
const columnas = 10
const valor_1_fila = ["$2.000","$4.400","$7.500","$11.400","$16.700","$24.000","$35.000","$53.300","$90.000","$200.000"]
const valor_2_fila = "$0"
const images = ["1tBaOrudcIjpM5Q3XUKRO5Dk3RZYuyIxv", "1eBhgh_PnGzErGAP51uUf2JgqNvkjoeDU", "1tRHVbl3A5spLRB4OkWeOmZhX_c8hTDOf", "1RDkOQMaxB7xKj7zgwROQEeMkFSJK02yT",
                "1dNWmuvN_nOxlkCme7jiwzzCDuRDgVt6D", "1pTGZ6tKGSv-vsYBkY0eV31KVHrsl8-Gs", "1qU2ZN5SeWMJBZpuByvnotjM6do9ZL-1G", "1beWYiw1qUxlLUKiu2SkIWp7BzD94NbBM",
                "1NU7u1qBko5f4q1pANULsmH6SuqZH2nyB", "10ZxGvd1hcxy1kXm3VCcw67Ueiy2C5Gcs"
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
  col2.innerHTML = '<input class="radio" data-toggle="modal" data-target="#staticBackdrop" onclick="clickaction()" type="radio" name="sgg_p4" value="'+(j+1)+'">';
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