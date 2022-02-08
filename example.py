import nano

wallet_seed = '7C41C84C4C88BA45F50753123292B29E9A6D762EFBEE70697C34BE77C3D4AF8E'
nano_address = 'nano_18yhiyzgz61w4678uxh5b1abphcwow5o1ki87eoj3uzwnefpm5idrhpub8yj'
index_pos = 0


#First Receive
result = nano.process_pending(nano_address, index_pos, wallet_seed)
print(result)

#Now send
dest_account = 'nano_1kd4h9nqaxengni43xy9775gcag8ptw8ddjifnm77qes1efuoqikoqy5sjq3'
raw_amount = 1000000000
result = nano.send_xrb(dest_account, raw_amount, nano_address, index_pos, wallet_seed)
print(result)
