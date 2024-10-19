from uagents import Agent, Context, Model

class Message(Model):
    message: str

bob = Agent(
    name="bob",
    port=8001,
    seed="01_agent_bob",  # Add this line if you want a consistent address
    endpoint=["http://127.0.0.1:8001/submit"],
)

# You'll need to replace this with Alice's actual address after running her
ALICE_ADDRESS = "agent1q2vl5wjtc8k2hhxkc0srhu9kl0ux5uju3mln8c63lgdzu83natuljq9cr5v"  # Replace with Alice's address

@bob.on_event("startup")
async def introduce(ctx: Context):
    ctx.logger.info(f"Bob's address: {ctx.address}")

@bob.on_interval(period=5.0)
async def send_to_alice(ctx: Context):
    ctx.logger.info(f"Sending message to Alice at {ALICE_ADDRESS}")
    await ctx.send(ALICE_ADDRESS, Message(message="Hello there, Alice!"))

@bob.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")

if __name__ == "__main__":
    bob.run()