// Nav Bar
$(window).scroll(function () {
    if ($(window).scrollTop() >= 200) {
        $('.kpi-nav').css('opacity',0);
    }
    if ($(window).scrollTop() >= 500) {
        $('.kpi-nav').addClass('fix');
        $('.kpi-nav').css('opacity',1);
    }
	if ($(window).scrollTop() <= 80) {
        $('.kpi-nav').removeClass('fix');
        $('.kpi-nav').css('opacity',1);
	}
});

// Menu Toggle
$('.tgl-menu').click(function () {
    $('.kpi-nav .tgl-menu').toggleClass('fa-bars fa-times');
    $(this).toggleClass('menu-active');
    $('.links').slideToggle();
})

// Search Toggle
$('.tgl-search').click(function () {
    $('.search-frm').slideDown();
    $(this).addClass('search-active');
})
$('.close-srch').click(function () {
    $('.search-frm').slideUp();
    $('.tgl-search').removeClass('search-active');
})






// Subject Menu
$('.subject-link').mouseenter(function () {
    $(".subject-link .tglSub").toggleClass('sub-link-active');
    $(".subject-menu").slideToggle();
})
$('.subject-link').mouseleave(function () {
    $(".subject-link .tglSub").toggleClass('sub-link-active');
    $(".subject-menu").slideToggle();
})
$(".subject-menu").mouseenter(function (e) {
    e.stopPropagation();
})
$(".subject-link").mouseleave(function () {
    $(".subject-link .tglSub").removeClass('sub-link-active');
    $(".subject-menu").slideUp();
    $('.subject-menu li .menu-subject').hide();
    $('.subject-menu li p').removeClass("sub-active");
})
$('.subject-menu li p').mouseenter(function () {
    $('.subject-menu li .menu-subject').hide();
    $('.subject-menu li p').removeClass("sub-active");
    $($(this).data('class')).slideToggle(400);
    $(this).addClass("sub-active");
})


// Webinar Menu
$('.tglWebinar').click(function () {

    $(".webinar-link").toggleClass('active');
    $(".webinar-menu").slideToggle();

    $('.kpi-nav').toggleClass('kpiNvA_Webinar');
    $('.kpi-nav').removeClass('kpiNvA_subject');

    $(".subject-link").removeClass('active');
    $(".subject-menu").slideUp();
})


// English Menu
$('.english-link').mouseenter(function () {

    $(".english-link .tglCours").toggleClass('sub-link-active');
    $(".english-menu").slideToggle();
})
$('.english-link').mouseleave(function () {

    $(".english-link .tglCours").toggleClass('sub-link-active');
    $(".english-menu").slideToggle();
})
$(".english-menu").mouseenter(function (e) {
    e.stopPropagation();
})
$(".english-link").mouseleave(function () {
    $(".english-link .tglCours").removeClass('sub-link-active');
    $(".english-menu").slideUp();

    $('.english-menu li .sub-enGli').hide();
    $('.english-menu li p').removeClass("sub-active");
})
$('.english-menu li p').mouseenter(function () {
    $('.english-menu li .sub-enGli').hide();
    $('.english-menu li p').removeClass("sub-active");
    $($(this).data('class')).slideToggle(400);
    $(this).addClass("sub-active");
})



// Technology Menu
$('.technology-link').mouseenter(function () {

    $(".technology-link .tglTech").toggleClass('sub-link-active');
    $(".technology-menu").slideToggle();
})
$('.technology-link').mouseleave(function () {

    $(".technology-link .tglTech").toggleClass('sub-link-active');
    $(".technology-menu").slideToggle();
})
$(".technology-menu").mouseenter(function (e) {
    e.stopPropagation();
})
$(".technology-link").mouseleave(function () {
    $(".technology-link .tglTech").removeClass('sub-link-active');
    $(".technology-menu").slideUp();

    $('.technology-menu li .sub-men').hide();
    $('.technology-menu li p').removeClass("sub-active");
})
$('.technology-menu li p').mouseenter(function () {
    $('.technology-menu li .sub-men').hide();
    $('.technology-menu li p').removeClass("sub-active");
    $($(this).data('class')).slideToggle(400);
    $(this).addClass("sub-active");
})


// Creative Menu
$('.creative-link').mouseenter(function () {

    $(".creative-link .Creatgl").toggleClass('sub-link-active');
    $(".creative-menu").slideToggle();
})
$('.creative-link').mouseleave(function () {

    $(".creative-link .Creatgl").toggleClass('sub-link-active');
    $(".creative-menu").slideToggle();
})
$(".creative-menu").mouseenter(function (e) {
    e.stopPropagation();
})
$(".creative-link").mouseleave(function () {
    $(".creative-link .Creatgl").removeClass('sub-link-active');
    $(".creative-menu").slideUp();

    $('.creative-menu li .sub-men').hide();
    $('.creative-menu li p').removeClass("sub-active");
})
$('.creative-menu li p').mouseenter(function () {
    $('.creative-menu li .sub-men').hide();
    $('.creative-menu li p').removeClass("sub-active");
    $($(this).data('class')).slideToggle(400);
    $(this).addClass("sub-active");
})


/* Carousel */
try {
    var owl = $('.owl-carousel');
    owl.owlCarousel({
        items:5,
        loop:true,
        margin:10,
        autoplay:true,
        autoplayTimeout:2000,
        autoplayHoverPause:true,
        responsiveClass:true,
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:2,
            },
            927:{
                items:3,
            },
            1000:{
                items:4,
            }
        }
    });   
}
catch (e) {
    console.log(e);
}