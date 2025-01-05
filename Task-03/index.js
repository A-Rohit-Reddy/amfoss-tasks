const buttonsounds={
    'w drum':"/sounds/crash.mp3",
    'a drum':"/sounds/kick-bass.mp3",
    's drum':"/sounds/snare.mp3",
    'd drum':"/sounds/tom-1.mp3",
    'j drum':"/sounds/tom-2.mp3",
    'k drum':"/sounds/tom-3.mp3",
    'l drum':"/sounds/tom-4.mp3",
};

function play(button){
    const soundfile=buttonsounds[button];
    if (soundfile){
        const audio = new Audio(soundfile);
        audio.play();
    }else{
        console.error('No sound file mapped for ${button}');
    }
}



