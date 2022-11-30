// Initialize Swiper starts
let swiper = new Swiper(".mySwiper", {
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  spaceBetween: 80,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
});
let swiper2 = new Swiper(".mySwiper2", {
  direction: "vertical",
  spaceBetween: 80,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
});

// Initialize Swiper ends

// page bar start

function getFetch() {
  fetch("http://127.0.0.1:8000/api/inventory/category/all/")
  .then(response => {
    console.log(response);
    if(!response.ok) {
      throw Error("Error")
    }
    return response.json();
  })
  .then(Alldata => {
    Alldata.forEach( data => {
      console.log(data);
      let barContainer = document.querySelector('.bar-container');
      let sideBar = document.querySelector('.side-bar');
      let ul = document.querySelector('.menu');
  
      let li = document.createElement("li")
      li.classList.add('item')
      ul.appendChild(li)
  
      let item_a = document.createElement("a")
      item_a.classList.add('item-a')
      item_a.innerText = `${data.name}`;
      item_a.setAttribute("href", `category/${data.slug}`)
      li.appendChild(item_a)
    });
  })
  .catch(error => {
    console.log(error);
  })
}
getFetch()

// page bar end

// arrow page start



// arrow page end

// preloader

// let loader = document.getElementById('preloader');
// window.addEventListener('load', function() {
//     loader.style.display = 'none'
// })