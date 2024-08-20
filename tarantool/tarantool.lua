box.cfg {
  listen = "0.0.0.0:3301"
}

if not box.schema.user.exists('admin') then
box.schema.user.create('admin', { password = 'presale' })
box.schema.user.grant('admin', 'read,write,execute', 'universe', nil, { if_not_exists = true })
end

if not box.space.tokens then
box.schema.space.create('tokens')
box.space.tokens:format({
  { name = 'token', type = 'string' },
  { name = 'username', type = 'string' },
  { name = 'password', type = 'string' }
})

box.space.tokens:create_index('primary', {
  type = 'hash',
  parts = { 1, 'string' }
})

box.space.tokens:insert({'token', 'admin', 'presale'})
end

if not box.space.data then
box.schema.space.create('data')
box.space.data:format({
  { name = 'key', type = 'string' },
  { name = 'value', type = 'string' }
})

box.space.data:create_index('primary', {
  type = 'hash',
  parts = { 1, 'string' }
})
end