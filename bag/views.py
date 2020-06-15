from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        # check if item in bag
        if item_id in list(bag.keys()):
            # if item in the bag, check if it is with the same id and size
            if size in bag[item_id]['items_by_size'].keys():
                # if it is add to the quantity of that item
                bag[item_id]['items_by_size'][size] += quantity
            else:
                # othewise set it equal to that quantity
                bag[item_id]['items_by_size'][size] = quantity
        else:
            # if item not in the bag, add it
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
