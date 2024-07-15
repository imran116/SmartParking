const menusToggler= document.querySelector(`.menusToggler`).addEventListener(`click`,(e)=>{
    document.querySelector(`.targetMenus`).classList.toggle(`menusToggleAnimation`)
})

const allRegisterOptionsToggler= document.querySelectorAll(`.registerOptionsToggler`)
allRegisterOptionsToggler.forEach((eachRegisterOptionsToggler)=>{

    eachRegisterOptionsToggler.addEventListener(`click`,(e)=>{
        document.querySelector(`.registerOptions`).classList.toggle(`registerOptionsAnimation`)
    })
})

document.querySelector(`.userTypestoggler`).addEventListener(`click`,()=>{
    document.querySelector(`.userTypes`).classList.toggle(`userTypesAnimation`)
})

// scroll top 
document.querySelector(`.goToTop`).addEventListener('click', e=>{
    document.documentElement.scrollTop=1;
})