def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session:
            carrito = request.session["carrito"]
            for key, value in carrito.items():
                total += int(value["precio"]) 
    return {"total_carrito": total}