let template = `<div class="schedule-card card"><p>Truck1</p><pclass="time"> ETA ${Math.random*6} min</p></div >`
for (let i = 1; i <= 10; i++) {
    if (Math.floor(Math.random() * 10) % 2 == 0){
        console.log(`<div class="schedule-card card"><p>Truck${i}</p><pclass="time"> ETA ${Math.floor(Math.random()*6)} min</p></div >`)
    }
    else  {
        console.log(`<div class="schedule-card card"><p>Available</p><pclass="time"> ${Math.floor(Math.random()*6)}pm min</p></div >`)
    }
}