var camera, scene, renderer, controls;
var geometry, material, mesh, land;

var objects = {};

var time = Date.now();

$(document).ready(function(){
    init();
    animate();
});

function setupGround(scene) {
    var geometry = new THREE.PlaneGeometry( 100, 100 );
    var planeMaterial = new THREE.MeshPhongMaterial( { color: 0xffdd99 } );
   // planeMaterial.ambient = planeMaterial.color;

    var ground = new THREE.Mesh( geometry, planeMaterial );

    ground.position.set( 0, 0, 0 );
    ground.rotation.x = - Math.PI / 2;
    ground.scale.set( 100, 100, 100 );

    ground.castShadow = false;
    ground.receiveShadow = true;

    scene.add( ground );
}
function init() {
    var canvas = document.getElementById("canvas");
    var canvasWidth = canvas.width;
    var canvasHeight = canvas.height;

    camera = new THREE.PerspectiveCamera( 75, canvasWidth/canvasHeight, 1, 10000 );
    camera.position.set(0,500,100);
    //camera.rotation.set(0,0,0);
    //camera.lookAt(new THREE.Vector3(0,0,0));

    scene = new THREE.Scene();

    renderer = new THREE.WebGLRenderer({canvas: canvas, antialias:true});
    renderer.shadowMapEnabled = true;

    setupGround(scene);

    geometry = new THREE.CubeGeometry( 100, 200, 200 );
    material = new THREE.MeshLambertMaterial( { color: 0xff0000} );

    mesh = new THREE.Mesh( geometry, material );
    mesh.position.set(0,200,-700);
    mesh.castShadow = true;
    mesh.receiveShadow = true;
    scene.add( mesh );


    // set up the sphere vars
    var radius = 50,
        segments = 30,
        rings = 30;

    // create a new mesh with
    // sphere geometry - we will cover
    // the sphereMaterial next!
    var sphereMaterial = new THREE.MeshLambertMaterial( { color: 0x00CC00 });

    var sphere = new THREE.Mesh( new THREE.SphereGeometry( radius, segments, rings), sphereMaterial);
    sphere.castShadow = true;
    scene.add(sphere);

    sphere.position.x = 0;
    sphere.position.y = 500;
    sphere.position.z = -500;

    // create a point light
   // var pointLight =
   //   new THREE.PointLight(0xFFFFFF);

    // set its position
   // pointLight.position.x = 10;
   // pointLight.position.y = 40;
    //pointLight.position.z = 130;

    // add to the scene
   // scene.add(pointLight);

   // var hemLight = new THREE.HemisphereLight(0x0000FF, 0x00FF00, 0.5);
   //scene.add(hemLight);

   // var directionalLight = new THREE.DirectionalLight( 0xffffff, 0.5 );
    //directionalLight.position.set( 0, 100, -100 );
    //scene.add( directionalLight );

   // var pointer = new THREE.PointerLockControls(camera);
    //pointer.enabled = true;
 //   scene.add(pointer);
    controls = new THREE.OrbitControls( camera );
   // controls.addEventListener( 'change', render );

   var light = new THREE.SpotLight( 0xffffff, 1, 0, Math.PI, 1 );
    light.position.set( 0, 1500, 1000 );
    light.target.position.set( 0, 0, -500 );

    light.castShadow = true;

    light.shadowCameraNear = 700;
    light.shadowCameraFar = camera.far;
    light.shadowCameraFov = 50;

    //light.shadowCameraVisible = true;

    light.shadowBias = 0.0001;
    light.shadowDarkness = 0.5;

    light.shadowMapWidth = 2048;
    light.shadowMapHeight = 1024;
    scene.add( light );


    var ambient = new THREE.AmbientLight( 0x444444 );
    scene.add( ambient );

    createMeshFromFile("testObject.js", "textObject");

}

function animate() {

    // note: three.js includes requestAnimationFrame shim
    requestAnimationFrame( animate );

    mesh.rotation.x += 0.01;
    mesh.rotation.y += 0.02;

    var testObject = objects["textObject"];
    if (testObject !== undefined) {
        testObject.rotation.x += 0.01;
         testObject.rotation.y += 0.02;
    }

    var now = Date.now();
    controls.update(now - time);

    time = now;
    render();
}

function render() {
    renderer.render( scene, camera );
}

function createMeshFromFile(filename, objectID) {
    var loader = new THREE.JSONLoader();
    loader.load( "models/"+filename, function(geometry, material){
      console.log("Loaded "+filename + " with geometry " + geometry + " and material "+ material);
     // var material = new THREE.MeshLambertMaterial({color: 0x666666});
      var filemesh = new THREE.Mesh(geometry, new THREE.MeshFaceMaterial(
        material ) );
      filemesh.position.set(0, 400, -300);
        filemesh.scale.set( 50, 50, 50);
        filemesh.castShadow = true;

      scene.add(filemesh);
      objects[objectID] = filemesh;
    });
}