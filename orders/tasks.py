from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    """
    Tâche pour envoyer une notification par e-mail lorsqu'une commande
    est créée avec succès.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Commande n° {order.id}' # type: ignore
    message = (
        f'Cher {order.first_name},\n\n'
        f'Vous avez passé une commande avec succès. '
        f'Votre numéro de commande est {order.id}.' # type: ignore
    )
    mail_sent = send_mail(
        subject,
        message,
        'admin@myshop.com',
        [order.email]
    )
    return mail_sent