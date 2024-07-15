// socityDashboard's Sidebar
const sideBarTogglers =document.querySelectorAll('.sideBarToggler')
const targetedMenus=document.querySelectorAll('.targetedMenu')
sideBarTogglers.forEach((eachSideBarToggler)=>{
    eachSideBarToggler.addEventListener('click',(e)=>{
      targetedMenus.forEach((eachMenu)=>{
        eachMenu.classList.toggle('targetedMenuEffect')
        document.querySelector('.sidebar').classList.toggle('sideBarEffect')
      })
        

        const allSideBarCLosers=document.querySelectorAll('.sideBarCloser')
        allSideBarCLosers.forEach((eachSideBarCloser)=>{
            eachSideBarCloser.classList.toggle('sideBarTogglerEffect')
        })

        const allSideBarOpeners=document.querySelectorAll('.sideBarOpener')
        allSideBarOpeners.forEach((eachSideBarOpener)=>{
            eachSideBarOpener.classList.toggle('sideBarTogglerEffect')
        })
    })
})

// socityDashboard's content tables

const statusCells=document.querySelectorAll('.statusCell')
statusCells.forEach((eachstStusCell)=>{
  if(eachstStusCell.innerHTML=='Active'){
    eachstStusCell.classList.add('bg-green-500')

  }else if(eachstStusCell.innerHTML=='Inactive'){
    eachstStusCell.classList.add('bg-red-600')

  }else if(eachstStusCell.innerHTML=='Upcoming'){
    eachstStusCell.classList.add('bg-yellow-500')
  }else null
})

// dashboardParkingMap's content Buttons

const parkingSlots = document.querySelectorAll(".parkingSlot");
parkingSlots.forEach((eachParkingSlot) => {
  if (eachParkingSlot.value == "available") {
    eachParkingSlot.classList.add("bg-green-600");
  } else if (eachParkingSlot.value == "soon") {
    eachParkingSlot.classList.add("bg-yellow-500");
    eachParkingSlot.setAttribute("disabled", true);
  } else {
    eachParkingSlot.classList.add("bg-red-600");
    eachParkingSlot.setAttribute("disabled", true);
  }
});