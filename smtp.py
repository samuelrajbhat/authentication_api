import smtplib
def prompt(title):
    return input(title).strip()

from_addr = prompt("From: ")
to_addrs = prompt("To: ")   
print("Enter your message. Press Ctrl-D (or Ctrl-Z on Windows) to end.")

lines = [f'From: {from_addr}', f"To: {', '.join(to_addrs)}",""]

while True:
    try:
        line = input()
    except EOFError:
        break
    else:
        lines.append(line)

msg = "\r\n".join(lines)
print("Message length:", len(msg))

server = smtplib.SMTP("localhost")
server.set_debuglevel(1)
server.sendmail(from_addr, to_addrs, msg)
server.quit()