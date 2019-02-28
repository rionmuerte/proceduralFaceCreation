# Procedural face generation

---

Let's talk about the benefits of not having to create new sprites or models for each of the characters we use. There are many games that use this.
Sometimes by allowing the user to create their own character which can be then saved as a hash string.
Same can be accomplished with entire bodies.
Most probably everyone reading this knows at least a few titles that employ such techniques.
But why would it be useful?
There are, perhaps as many reasons for using it as there are against.
I'll try to represent both sides of the argument in this case with annotated examples, presenting the easiest way to implement a simple random face generator.

---

#### Why and when?

---

There is no simple answer to the question "should I use procedurally generated characters in my project?".
There are many variables one needs to consider while trying to answer it.
Let's look at some advantages and disadvantages.
One can employ many different methods, I will, however, focus mostly on combining prefabricated assets into characters.


The most favourable argument is that it is possible to generate a huge amount of varied content with low resource input.
Let's say you need few background characters for a cutscene.
Making each and every one of those can often require a lot of work.
Now imagine a different solution. For simplicity's sake, we will use only a few variables.
Let's say, for our character to be unique, they need only a different nose a unique haircut.
In this case let's assume that we use `10` different hairstyles and `10` noses.
Using simple maths we can calculate that `noses x haircuts = 100`.
So at the moment we already have `100` different characters for a price of `20` assets.
Now compare it to creating every character by hand, it would take `100` models.
Doesn't matter if these are sprites, 3D models or anything else.
For this exact purpose we don't really need some fancy individual characters.
They will be unique on their own, just enough for background space fillers.
This allows us to generate them quickly and rather effortlessly.
If we make some error in the implementation, use too simple assets or just forget about something this could mean that all of our characters will look bad.
Having them procedurally generated doesn't ensure that they will look good.
In your game, you might need to mix various techniques.
Create different, elegant sprites for important characters, but leave the background noisy.


Procedural generation might save you a lot of space.
This includes RAM, and in that way it allows to store much more stuff in the memory, allowing game to load faster.
On the other hand, while we load assets faster, the CPU is burdened with extra work, which can result in longer loading times in the end.
In some cases, there might be work-arounds; however, if you are thinking about using it in your game, maybe you should delve deeper into this topic, ascertain what you need, how it would help and/or hinder your project in particular.
Remember there are many different ways to implement it - example below is but one of many.


Before that, however, I would like to present an argument against procedural generation.
The fact is that really only a part of things we generate will be good and/or unique.
Few will be able to tell apart characters whose eye-colour is the only differentiating factor.
This can happen if you do completely random things (like I do in this example).
Let's say you need to spawn a character but you already know their parents.
You can generate them in many different ways.
You could combine the features of both parents and add some noise.
Or you can go DNA style and make each component taken randomly from parents, for example.

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
