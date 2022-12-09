// Initialize Swiper starts
let swiper = new Swiper(".mySwiper", {
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
      keyboard: {
        enabled: true,
        onlyInViewport: false,
      },
    },
    spaceBetween: 80,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    keyboard: {
      enabled: true,
      onlyInViewport: false,
    },
  });
  let swiper2 = new Swiper(".mySwiper2", {
    direction: "vertical",
    spaceBetween: 80,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    keyboard: {
      enabled: true,
      onlyInViewport: false,
    },
  });
  
  // Initialize Swiper ends
  
  // page bar start
  
  function getFetch() {
    fetch("fetch.js")
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
        item_a.innerText = `${data.title}`;
        item_a.setAttribute("href", `${data.slug}`)
        li.appendChild(item_a)
      });
    })
    .catch(error => {
      console.log(error);
    })
  }
  getFetch()
  
  // page bar end
  