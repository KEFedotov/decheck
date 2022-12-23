from genie.testbed import load
from check_module import scheme_parse, check_out
from pyats import aetest
import logging

logger = logging.getLogger(__name__)

tb = load('./testbed.yaml')

print()
scheme = scheme_parse('./assessment/a3.yaml')
criterion = scheme['criterions'][0]
subcriteria = criterion['subcriteria'][0]
class Subcriteria_A2(aetest.Testcase):
        
    @aetest.test.loop(aspect=subcriteria['aspects'])
    def aspects_check(self, steps, aspect):
        global tb
        
        connections = aspect['check']['connections']
        
        for item in connections:
            try:
                tb.devices[item].connect(mit=True, log_stdout=False)
                logger.info(f'Connection to {item} successed')
            except:
                self.failed(f'Connection to {item} failed')
        
        with steps.start(f"+--- Aspect: {aspect['name']} - {aspect['description']}") as step:
            is_expected = True
            
            stages = aspect['check']['steps']
            
            for stage in stages:
                device = stage['device']
                command = stage['command']
                result = stage['result']

                try:
                    output = tb.devices[device].execute(command)
                    if result != 'None':
                        logger.error(f"DEVICE --{device}-- OUT")
                        logger.error(output)
                        logger.critical(stage['description'])
                        if not check_out(result, output):
                            is_expected = False
                except:
                    is_expected = False
                    break
            if is_expected:
                step.passed('Aspect passed')
            else:
                step.failed('Aspect failed')
    
    
if __name__ == "__main__":
    aetest.main()