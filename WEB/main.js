'use strict'

let langToggler = document.querySelector('.langs')
let langOptions = document.querySelector(".langs-con");
let snippets = document.querySelector('.snippets')
let langs = document.querySelectorAll('.lang')
let py = document.querySelector('.py')
let rb = document.querySelector(".rb");
let php = document.querySelector(".php");
let sh = document.querySelector(".sh");
let js = document.querySelector(".js");
let snpLangs = [py,rb,php,sh,js]
let langTitle = document.querySelector('#lang-title')
let tabs = document.querySelectorAll('.tab')
let responses = document.querySelectorAll('.response')


// programming language toggling

langToggler.addEventListener('click',()=>{
    langOptions.classList.toggle('hide')
    snippets.classList.toggle('blur')
})


langs.forEach((lang)=>{
    lang.addEventListener('click',(e)=>{
        
        langOptions.classList.toggle("hide");
        snippets.classList.toggle("blur");
        snpLangs.forEach(i =>{
            i.style.display = 'none'
        })

        let selected = e.currentTarget.dataset.lang;
        document.querySelector(`.${selected}`).style.display='block'
        langTitle.src = `${selected}.svg`;
    })
    
})


// response examples toggling

tabs.forEach(tab=>{
    tab.addEventListener('click',()=>{
        tabs.forEach(i=> i.classList.remove('clicked'))
        responses.forEach(r=>r.classList.add('off'))
        tab.classList.add('clicked')
        document.querySelector(`.${tab.dataset.tab}`).classList.remove('off')
    })


})

document.querySelector('#year').textContent = new Date().getFullYear()


document
  .querySelector(".dev_hire")
  .addEventListener(
    "click",
    () => (window.location.href = "https://www.fiverr.com/kimanxo_313")
  );

document
  .querySelector(".dev_support")
  .addEventListener(
    "click",
    () => (window.location.href = "https://www.buymeacoffee.com/kimanxo ")
  );

document
  .querySelector(".des_hire")
  .addEventListener(
    "click",
    () => (window.location.href = "https://www.fiverr.com/the_aminoz")
  );

document
  .querySelector(".des_support")
  .addEventListener(
    "click",
    () => (window.location.href = "https://www.buymeacoffee.com/djux")
  );

