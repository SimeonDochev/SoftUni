from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = [sub for sub in self.subscriptions if sub.id == subscription_id]
        if subscription:
            result = []
            subscription = subscription[0]
            customer = [cust for cust in self.customers if cust.id == subscription.customer_id][0]
            trainer = [trainer for trainer in self.trainers if trainer.id == subscription.trainer_id][0]
            plan = [p for p in self.plans if p.id == subscription.exercise_id][0]
            equipment = [e for e in self.equipment if e.id == plan.equipment_id][0]
            result.append(repr(subscription))
            result.append(repr(customer))
            result.append(repr(trainer))
            result.append(repr(equipment))
            result.append(repr(plan))
            return '\n'.join(result)
