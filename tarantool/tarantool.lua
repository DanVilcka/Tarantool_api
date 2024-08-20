box.cfg({
    listen = 3301
})

box.schema.space.create('test_space', {
    engine = 'vinyl',
    is_local = true,
})

box.space.test_space:create_index('primary', {
    parts = {1, 'unsigned'}
})

box.space.test_space:insert{1, 'Привет, мир!'}