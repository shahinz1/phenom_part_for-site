// navbar start

$(document).ready(function(){
    $('.navbar-toggler').click(function(){
        $('.navbar-collapse').slideToggle(300);
    });
    
    smallScreenMenu();
    let temp;
    function resizeEnd(){
        smallScreenMenu();
    }
  
    $(window).resize(function(){
        clearTimeout(temp);
        temp = setTimeout(resizeEnd, 100);
        resetMenu();
    });
  });
  
  const subMenus = $('.sub-menu');
  const menuLinks = $('.menu-link');
  
  function smallScreenMenu(){
    if($(window).innerWidth() <= 992){
        menuLinks.each(function(item){
            $(this).click(function(){
                $(this).next().slideToggle();
            });
        });
    } else {
        menuLinks.each(function(item){
            $(this).off('click');
        });
    }
  }
  
  function resetMenu(){
    if($(window).innerWidth() > 992){
        subMenus.each(function(item){
            $(this).css('display', 'none');
        });
    }
  }
  
  $(document).ready(function() {
  // Menentukan elemen yang dijadikan normal yaitu .normal
  var normalNavTop = $('.menutext').offset().top; 
  var normalNav = function(){
    var scrollTop = $(window).scrollTop();  
    // Kondisi jika discroll maka .nav ditambahkan class normal dan sebaliknya      
    if (scrollTop > normalNavTop) { 
        $('.menutext').css({ 'position': 'fixed', 'top':0, 'left':0, 'z-index':9999 });
    } else {
      $('.menutext').css({ 'position': 'relative' });
    }
  };
  
  // Jalankan fungsi
  normalNav();
  $(window).scroll(function() {
    normalNav();
  });
  });
  
  // sticky menu
  
  $(function () {
    $(document).scroll(function () {
      let $nav = $(".navbar");
      $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
  });
  
  let changeLogo = document.querySelector(".navbar-brand");
  let mainLogo = document.querySelector(".brand-logo");
  
  
  let myScrollFunc = function() {
    let y = window.scrollY;
    if (y >= 10) {
      mainLogo.style.display = "none";
      changeLogo.style.display = "block";
    } else {
      mainLogo.style.display = "block";
      changeLogo.style.display = "none";
    }
  };
  
  window.addEventListener("scroll", myScrollFunc);

