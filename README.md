# Procedural face generation

---

Lets talk about benefits of not having to create new sprite or model for each of the characters we use. Many games use this, sometimes in forrm of allowing user to create its own character copying later only some hash that represents his or hers face, or generating randomly faces, sometimes even whole bodies. This technique is used by plenty of games and probably everyone reading this knows at least few titles.  
But why is it usefull? There are plenty of reasons for using it, however there are maybe as well as many reasons not to use it. With examples from code and with some narration I'll try to show both sides arguments in this case, presenting also the easiest way to implement simple random face generator.

---

#### Why and when?

---

There is no simple answer to the question "shoul I use procedurally generated characters in my project?" There are many variables one needs to consider while trying to answer it. Lets look at some advantages and disadvantages if this idea. Because in procedural generation you can use many different methods I will focus mostly on combining prefabricated assets into characters.


First and most important argument is that with low resources you can create huge amount of different content. Lets say you need few characters in a cutscene, or for background in game. Making each and every one of those can be a lot of work and will require lots of characters. Now imagine different solution, for simplicity sake we will use only few variables. Let's say that our character to be unique needs only different nose and haircut. In this case lets say that we use `10` different hairstyles and `10` noses. By simple math we can calculate that `noses x haircuts = 100`. So at the moment we already have `100` different characters for a price of `20` assets. Now compare it to creating every character handmade, it would take `100` models to create them. No matter if this are sprites, 3D models or anything else. For this exact purpose we don't really need some fancy individual characters. They will be unique on their own, hwoever we don't need to really care how they look, they are just background space fillers. This allows to generate them quicly and rather painlessly. But in this case - having different characters doesnt mean that they will look good. And if we make some error in implementation, create to simple assets or just forget about something this could mean that all our characters will look bad. Having them procedurally generated doesn't mean that they will look good. In your game, you might need to mix both techniques. Create different, elegenat sprites for important characters, but leave the background to the noise.


Procedural generation might save you a lot of space. This includes RAM, and in that way it allows to store much more stuff in the memory, allowing game to load faster. On the other hand, at the same moment, while we are loading everything faster, CPU is forced to do some more work, effectively making loading sometimes longer. This might be worked around in some cases, however if you are thinking about using it in your game, maybe you should look into this topic too, see what you need, how does it help in your project and how it makes it worse. Remember that there are many different ways to do it, and the one presented below is only one of many.


However right now I would like to present some big argument against the idea of using procedural character generation, this is argument against procedural generation at all. Because let's face fact, that only part of things we do will be really good, or in some case really unique. not many people will even see that two different characters differ only with color of their eyes. This can happen if you do completely random things (like I do in this example). There are lots of methods, and many can be done to create some character. Let's say you need to spawn character but you already know its parents. You can make him in many different ways. You can combine features of both parents and add some random. Or you can go DNA style and make each component taken randomly from parents for example. Ways are many and it is you who needs to find best way to do so.

---

### But how to do it?

---

I think the simplest way to generate random face is to create few face components in my case `head shape`, `nose`, `mouth`, `eyes`, as well as some facial hair like `mustache`, `beard`, but also `haircut` and `eyebrows`. For this example purposes I used python language, because of how simple writing code for it is. The code is done mostly to explain how are things done, not necesairly to use it in some game, so you might need to translate it to work within your engine. And remember that this is not the only way to do it, probably your way will be much better, bcause it will be for YOUR game, this is only to show how does this simple method work. So how exactly are those things composed together?


First, the algorithm creates list of available components in each category. This is done in `__init__` method. Then we can call it to create random face, using `createRandomPicture(self, name):` we need only to give this picture name and all the magic begins. When we ask `pictureGenerator` class to make us a picture, it calls series of functions that build face for us and put it into the canvas. It create instance of `pictureHandler` class that handles operations on picture being created. Whenerver we call `addLayer` function it requires two arguments, first, `layer` is a path to layer as a png picture that will be used, second, `color` is tuple with three values representing RGB color (`#ffffff` is `white` and `#000000` is `black`). Function `colorBase` translates string of there values into color, this also adds onother functionality because it can darken or lighten color we are using, which I use while putting nose on face, I make it lighter so it won't blend in. Function `addLayer` puts then all pixels from selected layer into canvas, coloring them accordingly. Now putting it all together, calling `createRandomPicture` draws random face components and colors, then puts them on base picture, to save it at the end in `createdFaces` directory.

---

### Summary

---

Because this is one of the simplest ways to create random faces, it is far from perfect (maybe even it isn't good at all). It still needs some purpose, and probably many more work to make it available to work in your game. I did it as a proof of concept (and being bored one night) and most of the time I spent doing it was on making face parts. Because I am really bad in graphics it took long time. I calculated that having this set of *parts*, I can create 15000 rather different faces (at least composed from different assets, they look kinda the same thanks to my amazing drawing skills). Adding color palletes I used for coloring it rounds up in almost 5 million possible outcomes. Even though it isn't the best algorithm or it doesnt look really good, I encourage you to jump into topic of procedural generation of things in many cases, not only faces. This is extremally interesting topic and can bring big replayability into your game.


And for the end, I'd like to show you some examples of faces that could be made with this script and this set of assets.


![face1](https://github.com/rionmuerte/proceduralFaceCreation/blob/master/createdFaces/1.png)
![face2](https://github.com/rionmuerte/proceduralFaceCreation/blob/master/createdFaces/2.png)
![face3](https://github.com/rionmuerte/proceduralFaceCreation/blob/master/createdFaces/3.png)
![face4](https://github.com/rionmuerte/proceduralFaceCreation/blob/master/createdFaces/4.png)
![face5](https://github.com/rionmuerte/proceduralFaceCreation/blob/master/createdFaces/5.png)
