from Handlers import admin_handler, index_handler
# from Handlers.category__handler import CategoryHandler,CategoryEditHandler,CategoryDeleteHandler,CategoryNewHandler

urlList  = [
    (r'/admin', admin_handler.admin_Handler),
    (r'/', index_handler.index_Handler),
    (r'/register', index_handler.register_Handler),
    (r'/support', index_handler.support_Handler),
    (r'/forget_pass', index_handler.ForgetpassHandler),
    (r'/admin/payments', admin_handler.payments_Handler),
    (r'/admin/add_buy', admin_handler.add_buy_Handler),
    (r'/admin/delbuy', admin_handler.delbuy_Handler),
    (r'/admin/subscribers', admin_handler.subscribers_Handler),
    (r'/admin/subscribers/deluser', admin_handler.delsubscribers_Handler),
    (r'/modir', admin_handler.modir_Handler),
    (r'/user', admin_handler.user_Handler),
    (r'/logout', admin_handler.logout_Handler),
    (r'/admin/bill', admin_handler.bill_Handler),
    (r'/admin/tinyconsumption[/]?(\d+)?', admin_handler.tinyconsumption_Handler),
    (r'/admin/tinyconsumption/(page)', admin_handler.tinyconsumption_Handler, None, "admin_tinyconsumption"),
    (r'/profile', admin_handler.profile_Handler),
    (r'/UploadImageUser', admin_handler.UploadImageUserHandler),
    (r'/user/bill', admin_handler.user_bill_Handler),
    (r'/admin/message', admin_handler.message_Handler),
    (r'/user/registerbuy', admin_handler.registerbuy_Handler),
    (r'/admin/subscribers/changestatus', admin_handler.changestatus_Handler),
    (r'/admin/statusmessage', admin_handler.status_message_Handler),
    (r'/admin/delmessage', admin_handler.del_message_Handler),
    (r'/admin/note', admin_handler.note_Handler),
    (r'/user/note', admin_handler.note_Handler),
    (r'/admin/delnote', admin_handler.delnote_Handler),
    # (r'/user/tinyconsumption', admin_handler.tinyconsumption_Handler),
    (r'/user/tinyconsumption[/]?(\d+)?', admin_handler.tinyconsumption_Handler),
    (r'/user/tinyconsumption/(page)', admin_handler.tinyconsumption_Handler,None),

]