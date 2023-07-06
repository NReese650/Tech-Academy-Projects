// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your Javascript code.


// Get the video container element
var videoContainer = document.getElementById('video-container');

// Add event listeners for mouseover and mouseout
videoContainer.addEventListener('mouseover', function () {
    videoContainer.style.backgroundColor = 'blue';
});

videoContainer.addEventListener('mouseout', function () {
    videoContainer.style.backgroundColor = '';
});