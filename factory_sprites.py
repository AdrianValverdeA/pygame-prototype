# factory_sprites.py
import pygame

class FactorySprites:

    def __init__(self, prototypes, periods, event_type):

        self._prototypes = prototypes[:]
        self._periods = periods[:]
        self._event_types = []

        # Register events for each prototype
        for i, period in enumerate(self._periods):
            event = event_type + i
            self._event_types.append(event)
            pygame.time.set_timer(event, period)

    # Return a new instance cloned from prototype that corresponds
    # to this event type
    def make(self, event_type):
        idx = self._event_types.index(event_type)
        return self._prototypes[idx].clone()