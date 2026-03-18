jQuery(function ($) {
    'use strict'
    var supportsAudio = !!document.createElement('audio').canPlayType;
    if (supportsAudio) {
        // initialize plyr
        var player = new Plyr('#audio1', {
            controls: [                    
                // 'play',
                'progress',
                'current-time',
                'duration',
                'mute',
                'volume',
                // 'restart'
                
            ]
        });
        // initialize playlist and controls
        }
});


// Detial.html
    
        

