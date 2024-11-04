let slideIndex = 0;//tracks the first slide number
showSlides();//calls the showSlides 

function showSlides() {//controls slide visibility
  let slides = document.getElementsByClassName("myslides");
  let dots=document.getElementsByClassName("dot");
//   if (n>slides.length){slideIndex=1}//loops back to the first slide
//   if (n<1){slideIndex=slides.length}//loops to the last slide

  for (let i = 0; i < slides.length; i++) {//loops through all slides
    slides[i].style.display = "none";
  }

  slideIndex++;
  if(slideIndex>slideIndex.length){
    slideIndex=1;
  }
  slides[slideIndex-1].style.display = "block";//sets display to block for the current slide making it visible
 
  for(let i=0;i<dots.length;i++){//loops through all dots and removes the 'activate' class from each to reset their visual state
    dots[i].className=dots[i].className.replace("activate","");
  }
  dots[slideIndex-1].className+="activate";
  
 setTimeout(showSlides, 2000);//change slide after every 2 seconds
}
// increment or decrement the slide index by n
function plusSlides(n){
    slideIndex+=n-1;//updates the slide index and displays the new slide
    showSlides();
}

//set slideIndex directly to a specific slide number 
function currentSlide(n){
   slideIndex=n-1;
    showSlides();
}