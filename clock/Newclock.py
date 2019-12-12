var currentdate = new Date();
currentdate.getHours()


var hours = currentdate.getHours()

//With help from Paul S. from StackOverflow https://stackoverflow.com/questions/17003202/how-to-get-am-or-pm
//var hours = (hours+24-0)%24; 
    var mid='am';
    if(hours==0){ //At 00 hours we need to show 12 am
    hours=12;
    }
    else if(hours>12)
    {
    hours=hours%12;
    mid='pm';
    }
    //alert ('FredTime: ' + hours + mid);
//end of pauls help

//defining everything
//new p5.MediaElement(elt)
let vid;
let vid2;
let vid3;
let vid4;
let vid5;
let vid6;
let h;
let s;
let currentVideo;
let previousVideo;
let list1;
let list2;
let list3;
//end of defining everything


//create Video Refrence page
function setup() {
  noCanvas(400, 400);

  vid = createVideo(
    ['roadworkahead.mp4'],
    vidLoad
  );

  vid2 = createVideo(
    ['theycall.mp4'],
    vidLoad
  );
  
  vid3 = createVideo(
    ['bible.mp4'],  
    vidLoad
  );
  
  vid4 = createVideo(
    ['2bros.mp4'],  
    vidLoad
  );
  
  vid5 = createVideo(
    ['eve.mp4'],  
    vidLoad
  );
  
  vid6 = createVideo(
    ['chip.mp4'],  
    vidLoad
  );
  
  vid7 = createVideo(
    ['RedDress.mp4'],  
    vidLoad
  );
  vid8 = createVideo(
    ['Sprite.mp4'],
    vidLoad
  );

  vid9 = createVideo(
    ['mouse.mp4'],
    vidLoad
  );
  
  vid10 = createVideo(
    ['Backstreet.mp4'],  
    vidLoad
  );
  
  vid11 = createVideo(
    ['eep.mp4'],  
    vidLoad
  );
  
  vid12 = createVideo(
    ['pizza.mp4'],  
    vidLoad
  );
  
  vid13 = createVideo(
    ['wakeup.mp4'],  
    vidLoad
  );
  
  vid14 = createVideo(
    ['raccoon.mp4'],  
    vidLoad
  );
  vid15 = createVideo(
    ['who-are.mp4'],
    vidLoad
  );

  vid16 = createVideo(
    ['whoWant.mp4'],
    vidLoad
  );
  
  vid17 = createVideo(
    ['run.mp4'],  
    vidLoad
  );
  
  vid18 = createVideo(
    ['church.mp4'],  
    vidLoad
  );
  
  vid19 = createVideo(
    ['morning.mp4'],  
    vidLoad
  );
  
  vid20 = createVideo(
    ['scream-kid.mp4'],  
    vidLoad
  );
  
  vid21 = createVideo(
    ['dance-luke.mp4'],  
    vidLoad
  );
  
  vid22 = createVideo(
    ['adel-luke.mp4'],
    vidLoad
  );

  vid23 = createVideo(
    ['taco.mp4'],
    vidLoad
  );
  
  vid24 = createVideo(
    ['hello.mp4'],  //replace with new video file
    vidLoad
  );
  
  vid25 = createVideo(
    ['vodka.mp4'],  //replace with new video file
    vidLoad
  );
  
  vid26 = createVideo(
    ['Ah-mouse.mp4'],  //replace with new video file
    vidLoad
  );
  
  vid27 = createVideo(
    ['drop.mp4'],  //replace with new video file
    vidLoad
  );
  
  vid28 = createVideo(
    ['kush.mp4'],  
    vidLoad
  );
  
  vid29 = createVideo(
    ['kevin.mp4'],  
    vidLoad
  );
  
  vid30 = createVideo(
    ['kermit.mp4'],  
    vidLoad
  );
  
  vid31 = createVideo(
    ['fresh.mp4'],  
    vidLoad
  );
  
  vid32 = createVideo(
    ['dance.mp4'],
    vidLoad
  );

  vid33 = createVideo(
    ['chill.mp4'],
    vidLoad
  );
  
  vid34 = createVideo(
    ['wow.mp4'],  
    vidLoad
  );
  
  vid35 = createVideo(
    ['tort.mp4'],  
    vidLoad
  );
  
  vid36 = createVideo(
    ['mole.mp4'],  
    vidLoad
  );
  
  vid37 = createVideo(
    ['avacadothanks.mp4'],
    vidLoad
  );

  vid38 = createVideo(
    ['bannapeel.mp4'],
    vidLoad
  );
  
  vid39 = createVideo(
    ['breakingfree.mp4'],  
    vidLoad
  );
  
  vid40 = createVideo(
    ['chickens.mp4'],  
    vidLoad
  );
  
  vid41 = createVideo(
    ['chickenwing.mp4'],  
    vidLoad
  );
  
  vid42 = createVideo(
    ['crack.mp4'],  
    vidLoad
  );
  
  vid43 = createVideo(
    ['eveoprah.mp4'],  
    vidLoad
  );
  vid44 = createVideo(
    ['fuckyourchicken.mp4'],
    vidLoad
  );

  vid45 = createVideo(
    ['gir.mp4'],
    vidLoad
  );
  
  vid46 = createVideo(
    ['helliumballon.mp4'],  
    vidLoad
  );
  
  vid47 = createVideo(
    ['hello,itsme.mp4'],  
    vidLoad
  );
  
  vid48 = createVideo(
    ['lemons.mp4'],  
    vidLoad
  );
  
  vid49 = createVideo(
    ['magicmesh.mp4'],  
    vidLoad
  );
  
  vid50 = createVideo(
    ['merrycrisis.mp4'],  
    vidLoad
  );
  vid51 = createVideo(
    ['milkshakedance.mp4'],
    vidLoad
  );

  vid52 = createVideo(
    ['momcar.mp4'],
    vidLoad
  );
  
  vid53 = createVideo(
    ['mothertrucker.mp4'],  
    vidLoad
  );
  
  vid54 = createVideo(
    ['sandgaurdian.mp4'],  
    vidLoad
  );
  
  vid55 = createVideo(
    ['squashbanna.mp4'],  
    vidLoad
  );
  
  vid56 = createVideo(
    ['thepowerofchrist.mp4'],  
    vidLoad
  );
  
  vid57 = createVideo(
    ['yourtheone.mp4'],  
    vidLoad
  );
  
  vid58 = createVideo(
    ['a knife.mp4'],
    vidLoad
  );
  
  vid59 = createVideo(
    ['africadog.mp4'],  //replace with new video file
    vidLoad
  );
  
  vid60 = createVideo(
    ['bbq.mp4'],  //replace with new video file
    vidLoad
  );
  
  vid61 = createVideo(
    ['bitch.mp4'],  //replace with new video file
    vidLoad
  );
  
  vid62 = createVideo(
    ['dancedance.mp4'],  //replace with new video file
    vidLoad
  );
  
  vid63 = createVideo(
    ['dancepuppy.mp4'],  
    vidLoad
  );
  
  vid64 = createVideo(
    ['dancetildead.mp4'],  
    vidLoad
  );
  
  vid65 = createVideo(
    ['fork.mp4'],  
    vidLoad
  );
  
  vid66 = createVideo(
    ['graph.mp4'],  
    vidLoad
  );
  
  vid67 = createVideo(
    ['lipstick.mp4'],
    vidLoad
  );

  vid68 = createVideo(
    ['murder!.mp4'],
    vidLoad
  );
  
  vid69 = createVideo(
    ['oneyear.mp4'],  
    vidLoad
  );
  
  vid70 = createVideo(
    ['pancake.mp4'],  
    vidLoad
  );
  
  vid71 = createVideo(
    ['owl.mp4'],  
    vidLoad
  );
  
  vid72 = createVideo(
    ['redrobin.mp4'],
    vidLoad
  );

  vid73 = createVideo(
    ['singasong.mp4'],
    vidLoad
  );
  
  vid74 = createVideo(
    ['sleep.mp4'],  
    vidLoad
  );
  
  vid75 = createVideo(
    ['target.mp4'],  
    vidLoad
  );
  
  vid76 = createVideo(
    ['timetowakeup.mp4'],  
    vidLoad
  );
  
  vid77 = createVideo(
    ['turnoff.mp4'],  
    vidLoad
  );
  
  vid78 = createVideo(
    ['underthesea.mp4'],  
    vidLoad
  );
  vid79 = createVideo(
    ['wednsday.mp4'],
    vidLoad
  );

  
  
  //create video refrence page
  
  
  //Matt helped me create some arrays, I was using Python logic for Lists before he corrected me.
  h = hour();
  s = second();
  list1 = [vid6, vid14, vid23, vid25, vid28, vid31, vid35, vid36, vid33, vid38, vid41, vid37, vid60]; 
  //list1 is noon
  list2 = [vid, vid4, vid2, vid3, vid9, vid16, vid13, vid11, vid15, vid17, vid18, vid19, vid20, vid22, vid40, vid42, vid44, vid45, vid46, vid48, vid52, vid53, vid54, vid55, vid57, vid58, vid59, vid63, vid64, vid66, vid68, vid69, vid76];
  //list2 is morning
  list3 = [vid5, vid7, vid8, vid10, vid12, vid21, vid24, vid26, vid27, vid29, vid30, vid32, vid34, vid39, vid41, vid43, vid47, vid49, vid50, vid51, vid56, vid61, vid62, vid65, vid67, vid70, vid71, vid72, vid73, vid74, vid75, vid77, vid78, vid79]; 
  //list3 is evening
  
  vid.size(400, 400);
  
  //with Matts help I can now hide the videos, also kfrajer on Processing Forum helped with hiding and loading up the videos.   https://forum.processing.org/two/discussion/23870/p5js-problem-with-asynchronous-video-loading-playing
  
  vid.hide();
  vid2.hide();
  vid3.hide();
  vid4.hide(); 
  vid5.hide(); 
  vid6.hide(); 
  vid7.hide(); 
  vid8.hide();
  vid9.hide();
  vid10.hide();
  vid11.hide(); 
  vid12.hide(); 
  vid13.hide(); 
  vid14.hide(); 
  vid15.hide();
  vid16.hide();
  vid17.hide();
  vid18.hide(); 
  vid19.hide(); 
  vid20.hide(); 
  vid21.hide(); 
  vid22.hide();
  vid23.hide();
  vid24.hide();
  vid25.hide(); 
  vid26.hide(); 
  vid27.hide(); 
  vid28.hide(); 
  vid29.hide(); 
  vid30.hide(); 
  vid31.hide();
  vid32.hide();
  vid33.hide();
  vid34.hide(); 
  vid35.hide(); 
  vid36.hide(); 
  vid37.hide();
  vid38.hide();
  vid39.hide();
  vid40.hide(); 
  vid41.hide(); 
  vid42.hide(); 
  vid43.hide(); 
  vid44.hide();
  vid45.hide();
  vid46.hide();
  vid47.hide(); 
  vid48.hide(); 
  vid49.hide(); 
  vid50.hide(); 
  vid51.hide();
  vid52.hide();
  vid53.hide();
  vid54.hide(); 
  vid55.hide(); 
  vid56.hide(); 
  vid57.hide(); 
  vid58.hide();
  vid59.hide();
  vid60.hide(); 
  vid61.hide(); 
  vid62.hide(); 
  vid63.hide(); 
  vid64.hide(); 
  vid65.hide(); 
  vid66.hide();
  vid67.hide();
  vid68.hide();
  vid69.hide(); 
  vid70.hide(); 
  vid71.hide(); 
  vid72.hide();
  vid73.hide();
  vid74.hide();
  vid75.hide(); 
  vid76.hide(); 
  vid77.hide(); 
  vid78.hide(); 
  vid79.hide();
  
  
  
  vid.volume(0);
  vid2.volume(0);
  vid3.volume(0);
  vid4.volume(0);
  vid5.volume(0);
  vid6.volume(0);
  vid7.volume(0);
  vid8.volume(0);
  vid9.volume(0);
  vid10.volume(0);
  vid11.volume(0);
  vid12.volume(0);
  vid13.volume(0);
  vid14.volume(0);
  vid15.volume(0);
  vid16.volume(0);
  vid17.volume(0);
  vid18.volume(0);
  vid19.volume(0);
  vid20.volume(0);
  vid21.volume(0);
  vid22.volume(0);
  vid23.volume(0);
  vid24.volume(0);
  vid25.volume(0);
  vid26.volume(0);
  vid27.volume(0);
  vid28.volume(0);
  vid29.volume(0);
  vid30.volume(0);
  vid31.volume(0);
  vid32.volume(0);
  vid33.volume(0);
  vid34.volume(0);
  vid35.volume(0);
  vid36.volume(0);
  vid37.volume(0);
  vid38.volume(0);
  vid39.volume(0);
  vid40.volume(0);
  vid41.volume(0);
  vid42.volume(0);
  vid43.volume(0);
  vid44.volume(0);
  vid45.volume(0);
  vid46.volume(0);
  vid47.volume(0);
  vid48.volume(0);
  vid49.volume(0);
  vid50.volume(0);
  vid51.volume(0);
  vid52.volume(0);
  vid53.volume(0);
  vid54.volume(0);
  vid55.volume(0);
  vid56.volume(0);
  vid57.volume(0);
  vid58.volume(0);
  vid59.volume(0);
  vid60.volume(0);
  vid61.volume(0);
  vid62.volume(0);
  vid63.volume(0);
  vid64.volume(0);
  vid65.volume(0);
  vid66.volume(0);
  vid67.volume(0);
  vid68.volume(0);
  vid69.volume(0);
  vid70.volume(0);
  vid71.volume(0);
  vid72.volume(0);
  vid73.volume(0);
  vid74.volume(0);
  vid75.volume(0);
  vid76.volume(0);
  vid77.volume(0);
  vid78.volume(0);
  vid79.volume(0);
  
  
  
  //The hour function and a bit of tweaking with Matts help now the hour is specific to what time of day a video will load
  
  //below is more than 12, pm
    if (hour() > 12) {
      currentVideo = random(list3);
    }
//below is less than 12, am
    if (hour() < 12) {
      currentVideo = random(list2);
    }
    //currentVideo.show();
  //below is equal to 12, noon
    if (hour() == 12) {
      currentVideo = random(list1);
    }
    currentVideo.show();  
    currentVideo.loop();
    currentVideo.volume(1);
  
    }
  


//createVideo refrence
// This function is called when the video loads and so helpes with the sound in the video
function vidLoad() {
  //vid.loop();
  vid.volume(1);
  
  //vid2.loop();
  vid2.volume(1);
  
  //vid3.loop();
  vid3.volume(1);
  
  //vid4.loop();
  vid4.volume(1);
  
  //vid5.loop();
  vid5.volume(1);
  
  //vid6.loop();
  vid6.volume(1);
  
  //vid7.loop();
  vid7.volume(1); 
  
  vid8.volume(1);
  
  //vid2.loop();
  vid9.volume(1);
  
  //vid3.loop();
  vid10.volume(1);
  
  //vid4.loop();
  vid11.volume(1);
  
  //vid5.loop();
  vid12.volume(1);
  
  //vid6.loop();
  vid13.volume(1);
  
  //vid7.loop();
  vid14.volume(1); 
  
  vid15.volume(1);
  
  //vid2.loop();
  vid16.volume(1);
  
  //vid3.loop();
  vid17.volume(1);
  
  //vid4.loop();
  vid18.volume(1);
  
  //vid5.loop();
  vid19.volume(1);
  
  //vid6.loop();
  vid20.volume(1);
  
  //vid7.loop();
  vid21.volume(1); 
  
  vid22.volume(1);
  
  //vid2.loop();
  vid23.volume(1);
  
  //vid3.loop();
  vid24.volume(1);
  
  //vid4.loop();
  vid25.volume(1);
  
  //vid5.loop();
  vid26.volume(1);
  
  //vid6.loop();
  vid27.volume(1); 
  
  //vid5.loop();
  vid28.volume(1);
  
  //vid6.loop();
  vid29.volume(1);
  
  //vid7.loop();
  vid30.volume(1); 
  
  vid31.volume(1);
  
  //vid2.loop();
  vid32.volume(1);
  
  //vid3.loop();
  vid33.volume(1);
  
  //vid4.loop();
  vid34.volume(1);
  
  //vid5.loop();
  vid35.volume(1);
  
  //vid6.loop();
  vid36.volume(1); 
}

//createVideo Refrence

function draw() {
  h = hour();
  let m = minute();
  s = second();

  
   //duration method refrence
  //this makes sure that the video will switch to a new one after the hour is done
  if(currentVideo.time() >= currentVideo.duration())
  

    


  //if(h < hour()) //replace with s < second() to see what's happening every second instead of every hour
  {
    
    previousVideo = currentVideo;
    if (hour() > 12) {
      currentVideo = random(list3);
      
    }

    if (hour() < 12) {
      currentVideo = random(list2);
      
    }
    
    if (hour() == 12) {
      currentVideo = random(list1);
    }
    
    previousVideo.volume(0);
    previousVideo.hide();
    currentVideo.show();
   //currentVideo.loop();
    currentVideo.volume(1);
    currentVideo.stop();
    currentVideo.play();
  }

}
  
  
  
