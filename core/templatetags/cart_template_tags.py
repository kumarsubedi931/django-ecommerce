from django import template
from core.models import Order, Item
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0

@register.filter
def cart_items(user):
    if user.is_authenticated:
        order =  Order.objects.filter(user=user, ordered=False)
        item_li  = ""
        if  order.exists():
            for order_item in  order[0].items.all():
                item_li += """
                                <li class="header-cart-item">
                                        <div class="header-cart-item-img">
                                            <img src="{}" alt="IMG">
                            			</div>
                                        <div class="header-cart-item-txt">
                                            <a href="#" class="header-cart-item-name">
                                                {}
                                            </a>
                                            <span class="header-cart-item-info">
                                                ${}
                                            </span>
                                        </div>
                                    </li>
                            """.format(order_item.item.image.url,order_item.item.title,order_item.item.price)
            return mark_safe(item_li)
    return ""
