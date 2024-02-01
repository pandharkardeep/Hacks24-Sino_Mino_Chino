var tl=gsap.timeline();

tl.from(".navbar",{
    y:-100,
    duration:1,
    delay:0.9,
    opacity:0,
   stagger:0.5
})

tl.from(".left-body",{
    x:700,
    // y:300,
    duration:1,
    // rotate:360,
    opacity:0,
    stagger :0.3,
delay:1})



tl.from(".animate1", {
    x: -300,
    duration: 0.7,
    opacity: 0,
    stagger: 0.4,
    scrollTrigger: ".animate1"
});


tl.from(".box",{
    y:-200,
    duration:1,
    opacity:0,
    stagger:0.7,
    scrollTrigger:".box"

})

tl.from(".animate2",{
    x:-300,
    duration:0.7,
    opacity:0,
    stagger:0.4,
    scrollTrigger:".animate2"
})

tl.from(".faq-left",{
    x:-100,
    duration:0.4,
    opacity:0,
    scrollTrigger:".faq-left"
})

tl.from(".animate3",{
    y:-100,
    duration:0.4,
    opacity:0,
    stagger:0.2,
    scrollTrigger:".animate3"
})

tl.from(".left-body1",{
    x:-100,
    duration:1,
    delay:1,
    opacity:0,
    scrollTrigger:".left-body1"
})

tl.from(".right-body1",{
    x:100,
    duration:1,
    opacity:0,
    scrollTrigger:".right-body1"
})

tl.from(".first",{
    x:-100,
    duration:0.6,
    opacity:0,
    scrollTrigger:".first"
})

tl.from(".second ",{
    y:-100,
    duration:0.4,
    opacity:0,
    stagger:0.2,
    scrollTrigger:".second"
})

tl.from(".third ",{
    y:-100,
    duration:0.4,
    opacity:0,
    stagger:0.2,
    scrollTrigger:".third"
})

tl.from(".forth ",{
    y:-100,
    duration:0.4,
    opacity:0,
    stagger:0.2,
    scrollTrigger:".forth"
})


