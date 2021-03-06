from config import command_prefix, builtin_commands
from core.command_factory import command_key, builtin_command_key, prefixless_commands
assert not any(c.isspace() for c in command_prefix)

def msg_parser(msg): # None means no response
    do_response = do_message_response(msg)
    if do_response[0]:
        msg_body = do_response[1]
        command = msg_body[0]
        no_prefix_command = command[1:]
        if no_prefix_command in command_key:
            command_body = "" if len(msg_body) == 1 else msg.content[len(command):].strip()
            msg.body = command_body
            return command_key[no_prefix_command](msg)
        if no_prefix_command in builtin_commands.values():
            return builtin_command_key[no_prefix_command](msg)
    return None

def prefixless_parser(msg):
    return [func(msg) for func in prefixless_commands if func(msg) is not None]

def do_message_response(msg):
    splitted_message = msg.content.split()
    do_resp = len(splitted_message) != 0 and len(splitted_message[0]) > 1 and splitted_message[0][0] == command_prefix
    return (do_resp, splitted_message)
