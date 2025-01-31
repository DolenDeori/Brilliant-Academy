// get stream 
var stream = document.getElementsByName('stream');

// check btn 
var check_btn = document.getElementById('check_btn');

// inputbox
var input_box_stream = document.getElementById('slected_stream');
var input_box_subjects = document.getElementById('slected_subjects');

// get integrated subjects
var subject_in = document.getElementsByName('subject_in');

// get general science subjects
var subject_gs = document.querySelectorAll('.subject_gs');

// get art subjects 
var subject_ar = document.querySelectorAll('.subject_ar')


// option in integrated science
var medical = document.getElementById('Medical')
var engineering = document.getElementById('Engineering')

// Option in general science 
var Maths = document.getElementById('Maths');
var Antroplogy = document.getElementById('Antroplogy');
var Biology = document.getElementById('Biology');
var Economics = document.getElementById('Economics');
var statistics = document.getElementById('statistics');

// Option for arts 
var Anthropology = document.getElementById('Anthropology');
var Sociology = document.getElementById('Sociology');

// function for subjects to enable
function enable_diable_stream_subjects(enable1 , disable1 , disable2){
    var count;
    for(count = 2 ; count < enable1.length ; count++ ){
        enable1[count].disabled = false;
    }
    for(count = 2 ; count < disable1.length ; count++ ){
        disable1[count].disabled = true;
    }
    for(count = 2 ; count < disable2.length ; count++ ){
        disable2[count].disabled = true;
    }
}

var streams;
for (streams = 0 ; streams < stream.length ; streams++){
    stream[streams].addEventListener('click' , function(){
        if(stream[0].checked){
            stream[0].disabled = true
            stream[1].disabled = false
            stream[2].disabled = false
            enable_diable_stream_subjects(subject_in , subject_gs , subject_ar);
        }
        else if(stream[1].checked){
            stream[1].disabled = true
            stream[2].disabled = false
            stream[0].disabled = false
            enable_diable_stream_subjects(subject_gs , subject_ar , subject_in);
        }
        else if(stream[2].checked){
            stream[1].disabled = false
            stream[2].disabled = true
            stream[0].disabled = false
            enable_diable_stream_subjects(subject_ar , subject_in , subject_gs);
        }
    })
}

var txt;
// for integreted science 
stream.forEach((streams) => {
    streams.addEventListener('click' , function(){
        if (streams.checked == true){
            if(streams.value == 'Integrated'){
                input_box_stream.value = streams.value
                input_box_subjects.value = ''
                txt = []
                subject_in.forEach((subject) =>{
                    if(subject.checked == true){
                        if(subject.disabled == false){
                            subject.checked = false
                        }
                    }
                    else{
                        subject.addEventListener('click' , function (){
                            if(subject.checked == true){
                                txt.push(subject.value)
                            }
                            else{
                                remove_item = txt.indexOf(subject.value);
                                txt.splice(remove_item , 1);
                            }
                            input_box_subjects.value = txt.toString();
                            console.log(input_box_subjects.value)
                        })
                    }
                })
            }

            else if (streams.value == 'General Science'){
                input_box_stream.value = streams.value;
                input_box_subjects.value = '';
                txt = []
                subject_gs.forEach((subject) =>{
                    if(subject.checked == true){
                        if(subject.disabled == false){
                            subject.checked = false;
                        }
                    }
                    else{
                        subject.addEventListener('click' , function (){
                            if(subject.checked == true){
                                txt.push(subject.value)
                            }
                            else{
                                remove_item = txt.indexOf(subject.value);
                                txt.splice(remove_item , 1);
                            }
                            // console.log(list)
                            input_box_subjects.value = txt;
                            input_box_subjects.setAttribute('value' , txt.toString())
                            console.log(input_box_subjects.value)
                        })
                    }
                })
            }

            else if (streams.value == 'Arts'){
                input_box_stream.value = streams.value;
                input_box_subjects.value = '';
                txt = []
                subject_ar.forEach((subject) =>{
                    if(subject.checked == true){
                        if(subject.disabled == false){
                            subject.checked = false;
                        }
                    }
                    else{
                        subject.addEventListener('click' , function (){
                            if(subject.checked == true){
                                txt.push(subject.value)
                            }
                            else{
                                remove_item = txt.indexOf(subject.value);
                                txt.splice(remove_item , 1);
                            }
                            // console.log(list)
                            // console.log(subject_ar)
                            console.log(txt)
                            input_box_subjects.value = txt.toString();
                        })
                    }
                })
            }
        }
    })
})
 
// for options in subjects of streams
function enable_disable(enable , disable){
    if(enable.checked == true){
        disable.disabled = true
        disable.required = false
    }
    else{
        disable.disabled = false
        disable.required = true
    }
}

// Options in intregrated science
medical.addEventListener('click' , function(){
    enable_disable(medical , engineering);
})

engineering.addEventListener('click' , function(){
    enable_disable(engineering , medical);
})


// options in general science 
Maths.addEventListener('click' , ()=>{
    enable_disable(Maths , Antroplogy);
})
Antroplogy.addEventListener('click' , ()=>{
    enable_disable(Antroplogy , Maths);
})

Biology.addEventListener('click' , ()=>{
    enable_disable(Biology , Economics);
    enable_disable(Biology , statistics);
})

statistics.addEventListener('click' , ()=>{
    enable_disable(statistics , Biology)
    enable_disable(statistics , Economics)
})

Economics.addEventListener('click' , ()=>{
    enable_disable(Economics , Biology);
    enable_disable(Economics , statistics);
})

// options in arts 
Anthropology.addEventListener('click' , ()=>{
    enable_disable(Anthropology , Sociology)
})

Sociology.addEventListener('click' , ()=> {
    enable_disable(Sociology , Anthropology);
})


function limit_click(){
    var newvar = 0
    for (var sub = 2 ; sub < subject_ar.length ; sub++ ){
        if(newvar < 4){
            if(subject_ar[sub].checked == true){
                newvar = newvar + 1
            }
        }
        else{
            subject_ar.forEach((item) =>{
                if(item.checked == false){
                    item.disabled = true
                    document.getElementById('message').innerHTML = 'maximum value reached';
                    return true;
                }
            })
        }
    }
}