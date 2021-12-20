var images = document.getElementsByTagName('img');
var image_string = "";

for(var i = 0; i < images.length; i++) {
    image_string += images[i].src + "\n";
}

console.log(image_string);
