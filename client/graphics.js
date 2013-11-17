var camera, scene, renderer, controls;
var geometry, material, mesh, land;
var time = Date.now();

$(document).ready(function(){
    init();
    animate();
});

function init() {
    var canvas = document.getElementById("canvas");
    var canvasWidth = canvas.width;
    var canvasHeight = canvas.height;
    camera = new THREE.PerspectiveCamera( 75, canvasWidth/canvasHeight, 1, 10000 );
    camera.position.set(0,500,100);
    //camera.rotation.set(0,0,0);
//camera.lookAt(new THREE.Vector3(0,0,0));
    scene = new THREE.Scene();

    geometry = new THREE.CubeGeometry( 100, 200, 200 );
    material = new THREE.MeshLambertMaterial( { color: 0xff0000} );

    mesh = new THREE.Mesh( geometry, material );
    mesh.position.set(0,200,-700);
    scene.add( mesh );

    renderer = new THREE.WebGLRenderer({canvas: canvas, antialias:true});


    // set up the sphere vars
    var radius = 50,
        segments = 30,
        rings = 30;

    // create a new mesh with
    // sphere geometry - we will cover
    // the sphereMaterial next!
    var sphereMaterial =
  new THREE.MeshLambertMaterial(
    {
      color: 0x00CC00
    });

    var sphere = new THREE.Mesh(
        new THREE.SphereGeometry(
        radius,
        segments,
        rings),
        sphereMaterial);

    // add the sphere to the scene
    scene.add(sphere);

    sphere.position.x = 0;
    sphere.position.y = 50;
    sphere.position.z = -500;

    // create a point light
    var pointLight =
      new THREE.PointLight(0xFFFFFF);

    // set its position
    pointLight.position.x = 10;
    pointLight.position.y = 40;
    pointLight.position.z = 130;

    // add to the scene
    scene.add(pointLight);

    var landgeometry = new THREE.CubeGeometry( 5000, 100, 5000 );
    var landmaterial = new THREE.MeshLambertMaterial( { color: 0xCCCCCC} );
    land = new THREE.Mesh(landgeometry, landmaterial);
    land.position.set(0,-50,-2500);
    scene.add(land);

    //var hemLight = new THREE.HemisphereLight(0x0000FF, 0x00FF00, 0.5);
   //scene.add(hemLight);

    var directionalLight = new THREE.DirectionalLight( 0xffffff, 0.5 );
    directionalLight.position.set( 0, 100, -100 );
    scene.add( directionalLight );

   // var pointer = new THREE.PointerLockControls(camera);
    //pointer.enabled = true;
 //   scene.add(pointer);
    controls = new THREE.OrbitControls( camera );
   // controls.addEventListener( 'change', render );
}

function animate() {

    // note: three.js includes requestAnimationFrame shim
    requestAnimationFrame( animate );

    mesh.rotation.x += 0.01;
    mesh.rotation.y += 0.02;

    var now = Date.now();
   // console.log (now + " " + time);
    controls.update(now - time);

    time = now;

    render();


    //console.log(camera.position);


}


function render() {
    renderer.render( scene, camera );

}