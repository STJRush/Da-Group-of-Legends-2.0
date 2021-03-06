from time import sleep

print("Do you want to bake something? or do you want to cook something?")
cookorbake=input("Type bake or cook")

if cookorbake == "bake" :
    bake=input("What do you want to bake?")
    if bake == "spongecake":
        print("To make spongecake you will need, 225g (8 oz) self-raising flour, 225g (8 oz) butter, at room temperature, 225g (8 oz) caster sugar, 4 eggs, 1 teaspoon baking powder")
        sleep(8)
        print("1. Preheat the oven to 180 degrees C / gas mark 4.")
        sleep(2)
        print("2. Measure all the ingredients into a large bowl.")
        sleep(2)
        print("3. Mix all of the ingredients using a electric whisk.")
        sleep(2)
        print("4. Pour the mixture into 2 non-stick 7 inch (18cm) tins.")
        sleep(2)
        print("5. Place them in the oven till golden brown 15-25 minutes.")
        sleep(2)
        print("6. Cool on a wire rack before serving.")
    elif bake == "banana bread":
        print("To make the banana bread you will need, 2 to 3 very ripe bananas, peeled, 1/3 cup melted butter, 1 teaspoon baking soda, Pinch of salt, 3/4 cup sugar (1/2 cup if you would like it less sweet, 1 cup if more sweet), 1 large egg, beaten, 1 teaspoon vanilla extract, 1 1/2 cups of all-purpose flour.")
        sleep(10)
        print("1 Preheat the oven to 350°F (175°C), and butter a 4x8-inch loaf pan.")
        sleep(5)
        print("2 In a mixing bowl, mash the ripe bananas with a fork until completely smooth. Stir the melted butter into the mashed bananas")
        sleep(5)
        print("3 Mix in the baking soda and salt. Stir in the sugar, beaten egg, and vanilla extract. Mix in the flour.")
        sleep(5)
        print("4 Pour the batter into your prepared loaf pan. Bake for 50 minutes to 1 hour at 350°F (175°C), or until a tester inserted into the center comes out clean.")
        sleep(6)
        print("Remove from oven and let cool in the pan for a few minutes. Then remove the banana bread from the pan and let cool completely before serving. Slice and serve. (A bread knife helps to make slices that aren't crumbly.)")
    elif bake == "scones" :
       print("To make scones you will need 375g plain flour, 100g caster sugar, 5 teaspoons baking powder, 1/2 teaspoon salt, 170g butter, 1 egg, beaten, 225ml milk")
       sleep(10)
       print("1. Preheat oven to 200 C / Gas 6. Lightly grease a baking tray.")
       sleep(3)
       print("2. In a large bowl, combine flour, sugar, baking powder and salt. Rub in butter. Mix the egg and milk in a small bowl, and stir into flour mixture until moistened.")
       sleep(5)
       print("3. Turn dough out onto a lightly floured surface, and knead briefly. Roll dough out into a 2cm thick round. Cut into 8 wedges, and place on the prepared baking tray.")
       sleep(5)
       print("Bake 15 minutes in the preheated oven, or until golden brown.")
    else :
        print("Sorry that recipe isn't on our baking memory!")

elif cookorbake == "cook" :
    cook=input("What do you want to cook?")
    if cook == "chicken curry" :
        print("For the ingredients you will need 1 large onion")
        sleep(2)
        print("50g ginger, roughly chopped")
        sleep(2)
        print("4tbsp vegetably oil")
        sleep(2)
        print("2tsp cumin seed")
        sleep(2)
        print("1tsp fennel seed")
        sleep(2)
        print("5cm cinnamon stick")
        sleep(2)
        print("1tsp chilli flakes")
        sleep(2)
        print("1 tsp garam masala")
        sleep(2)
        print("1tsp turmeric")
        sleep(2)
        print("1tsp caster sugar")
        sleep(2)
        print("400g can chopped tomatoes")
        sleep(2)
        print("8 chicken thighs, skinned, boneless")
        sleep(2)
        print("250ml hot chicken stock")
        sleep(2)
        print("2tbsp chopped coriander")
        sleep(2)
        print("1. Roughly chop the onion, transfer to a small food processor, and add 3 tablespoons of water - process to a slack paste. You could use a stick blender for this or coarsely grate the onion into a bowl – there’s no need to add any water if you are grating the onion. Tip into a small bowl and leave on one side.")
        sleep(10)
        print("2. Put the chopped garlic and ginger into the same food processor and add 4 tbsp water – process until smooth and spoon into another small bowl. Alternatively, crush the garlic to a paste with a knife or garlic press and finely grate the ginger.")
        sleep(10)
        print("3. Heat the oil in a wok or sturdy pan set over a medium heat. Combine the cumin and fennel seeds with the cinnamon and chilli flakes and add to the pan in one go. Swirl everything around for about 30 secs until the spices release a fragrant aroma.")
        sleep(10)
        print("4. Add the onion paste – it will splutter in the beginning. Fry until the water evaporates and the onions turn a lovely dark golden - this should take about 7-8 mins. Add the garlic and ginger paste and cook for another 2 mins – stirring all the time.")
        sleep(10)
        print("5. Stir in the garam masala, turmeric, and sugar and continue cooking for 20 secs before tipping in the tomatoes. Continue cooking on a medium heat for about 10 mins without a lid until the tomatoes reduce and darken.")
        sleep(8)
        print("6. Cut the chicken thighs into 3cm chunks and add to the pan once the tomatoes have thickened to a paste. Cook for 5 mins to coat the chicken in the masala and seal in the juices, and then pour over the hot chicken stock. Simmer for 8-10 mins without a lid until the chicken is tender and the masala lightly thickened – you might need to add an extra ladleful of stock or water if the curry needs it. Sprinkle with chopped coriander and serve with Indian flatbreads or fluffy basmati rice and a pot of yogurt on the side.")
        sleep(15)
