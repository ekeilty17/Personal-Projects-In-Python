from image_to_tupper import *
import matplotlib.pyplot as plt


K_Tupper = 4858450636189713423582095962494202044581400587983244549483093085061934704708809928450644769865524364849997247024915119110411605739177407856919754326571855442057210445735883681829823754139634338225199452191651284348332905131193199953502413758765239264874613394906870130562295813219481113685339535565290850023875092856892694555974281546386510730049106723058933586052544096664351265349363643957125565695936815184334857605266940161251266951421550539554519153785457525756590740540157929001765967965480064427829131488548259914721248506352686630476300

def tupper_plot(K, H=17, W=106, filename='tupper'):
    
    if type(K) == str:
        # height of characters = 9
        # width of each character = 7
        # the +1 is to account for the spaces
        H = 9
        W = len(K)*(7+1)
        print W
        K = string_to_tupper(K.upper())

    def tupper(x,y):
        return 0.5 < ((y//H) // (2**(H*x + y%H))) % 2

    # plotting
    plot.rc('patch', antialiased=False)
    print 'Plotting...'
    for x in xrange(W):
        print 'Column %d...' % x
        for yy in xrange(H):
            y = K + yy
            if tupper(x,y):
                plt.bar(x=x, bottom=yy, height=1, width=1, linewidth=0, color='black')
    print 'Done plotting'

    # Making axes look nice
    plt.axis('scaled')
    # For large graphs, must change these values (smaller font size, wider-apart ticks)
    buf = 2
    plt.xlim((-buf,W+buf))
    plt.ylim((-buf,H+buf))
    plt.rc('font', size=20)
    plt.xticks(range(0, W, 5))
    yticks = range(0, H+1, H)
    plt.yticks(yticks, ['K']+['K + %d'%i for i in yticks][1:])
    #plt.savefig(filename = '.png')
    plt.show()
    
    return K

#tupper_plot(K_Tupper)
#S = "abcdefghijklmnopqrstuvwxyz"
S = "Kosar Hedayat"
print tupper_plot(S)
